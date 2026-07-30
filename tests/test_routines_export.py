# -*- coding: utf-8 -*-
"""The exported routines (agents/routines/) must stay portable and installable.

These pin the properties that make a second machine work — and specifically the four
defects the export shipped with on 2026-07-30:

  * routines.json pointed at a "$schema" file that did not exist;
  * displayName was dropped, so an installed routine appeared unnamed and lost the
    1./2./3. ordering prefixes the maintainer relies on;
  * useWorktree was dropped, so a routine's execution mode did not survive the trip;
  * --register wrote entries missing createdAt / displayName / useWorktree, and
    export inferred the repo path with os.path.commonpath, which silently yields a
    PARENT directory when two routines have different working directories.

Nothing here touches the live app registry, so it runs the same in CI as locally.
"""
from __future__ import annotations

import importlib.util
import io
import json
import os
import pathlib
import re
import contextlib
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parents[1]
RD = REPO / "agents" / "routines"
MANIFEST = json.loads((RD / "routines.json").read_text(encoding="utf-8"))
ROUTINES = MANIFEST["routines"]
TOKENS = {"{{REPO}}", "{{PLATFORM_NOTE}}"}
MAC_NOTE = ("On macOS use `python3` (not `python`); "
            "PYTHONIOENCODING=utf-8 is unnecessary but harmless.")


def _load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def exp():
    return _load("export_routines", RD / "export_routines.py")


@pytest.fixture
def inst():
    return _load("install_routines", RD / "install_routines.py")


@pytest.fixture
def inst_disabled(inst_sandbox):
    """The installer with one deliberately disabled cron routine added to its manifest.

    No live routine is disabled any more — the retired `agent-lab-daily-posts` was deleted
    on 2026-07-31 — but the installer still has to handle a disabled entry correctly, and
    that handling is load-bearing: the registration tool cannot set an enabled flag, so a
    disabled routine must never be requested with a live schedule. Synthesize the case
    rather than let deleting a routine quietly turn these tests into skips.
    """
    inst, prompts, manifest = inst_sandbox
    tid = "retired-cron-routine"
    (prompts / f"{tid}.md").write_text("body in {{REPO}} — {{PLATFORM_NOTE}}\n", encoding="utf-8")
    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["routines"].append({
        "id": tid, "displayName": "9. Retired routine", "description": "a retired cron routine",
        "schedule": "cron:0 7 * * *", "enabled": False, "useWorktree": False, "cwd": "{{REPO}}",
    })
    manifest.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return inst, tid


# --------------------------------------------------------------------------- manifest

def test_manifest_has_no_dangling_schema_pointer():
    """Every path the manifest references must resolve."""
    for key, value in MANIFEST.items():
        if key == "routines" or not isinstance(value, str):
            continue
        if value.startswith("./") or value.endswith((".md", ".json")):
            assert (RD / value).exists(), f"{key} -> {value} does not exist"


def test_manifest_entries_carry_the_definitional_fields():
    assert ROUTINES, "the manifest must not be empty"
    for r in ROUTINES:
        assert set(r) == {"id", "displayName", "description", "schedule",
                          "enabled", "useWorktree", "cwd"}, r["id"]
        assert r["cwd"] == "{{REPO}}", r["id"]
        assert isinstance(r["enabled"], bool) and isinstance(r["useWorktree"], bool)
        assert r["schedule"] == "manual" or r["schedule"].startswith(("cron:", "once:"))


def test_every_routine_has_a_display_name():
    """All five are named, so a blank one means an export ran on a machine whose app had
    not been given the names — which silently drops them from the record."""
    unnamed = [r["id"] for r in ROUTINES if not r["displayName"]]
    assert not unnamed, f"no display name (exported from an unconfigured machine?): {unnamed}"


def test_display_name_prefixes_do_not_collide():
    """The maintainer orders the sidebar with numeric prefixes, so two routines claiming
    the same number is ambiguous — and it is how a retired routine ends up sitting in the
    live run order."""
    named = [r["displayName"] for r in ROUTINES if r["displayName"]]
    prefixes = [n.split(".")[0].strip() for n in named]
    dupes = {p for p in prefixes if prefixes.count(p) > 1}
    assert not dupes, f"display-name prefixes collide: {sorted(dupes)} in {sorted(named)}"


def test_manifest_and_prompts_are_in_one_to_one_correspondence():
    on_disk = {p.stem for p in (RD / "prompts").glob("*.md")}
    assert on_disk == {r["id"] for r in ROUTINES}


# --------------------------------------------------------------------------- prompts

@pytest.mark.parametrize("prompt", sorted((RD / "prompts").glob("*.md")), ids=lambda p: p.stem)
def test_prompt_is_portable(prompt: pathlib.Path):
    text = prompt.read_text(encoding="utf-8")
    assert set(re.findall(r"\{\{[A-Z_]+\}\}", text)) <= TOKENS
    for token in TOKENS:                      # both must be present, or the export is lossy
        assert token in text, f"{prompt.name} lost {token}"
    for leak in ("C:" + chr(92), "C:/", "/Users/", "/home/"):
        assert leak not in text, f"{prompt.name} leaks an absolute machine path: {leak}"
    assert "Windows" not in text, f"{prompt.name} hard-codes a Windows-only instruction"
    # A prompt may instruct ("do not rely on the gh CLI"). It must not assert a fact about
    # whichever machine it was exported from: that claim travels and stops being true.
    for claim in ("is NOT installed", "is not installed", "is unavailable",
                  "not available on this machine"):
        assert claim not in text, f"{prompt.name} asserts a machine fact: {claim!r}"
    assert prompt.read_bytes().count(b"\r\n") == 0, f"{prompt.name} must be LF"


def test_manifest_is_lf_so_the_export_is_platform_independent():
    assert (RD / "routines.json").read_bytes().count(b"\r\n") == 0


# --------------------------------------------------------------------------- export

def test_detect_repo_refuses_to_guess_a_parent_of_divergent_checkouts(exp):
    """os.path.commonpath would return the PARENT here, corrupting every {{REPO}}."""
    with pytest.raises(SystemExit) as e:
        exp.detect_repo([{"cwd": "/a/one"}, {"cwd": "/a/two"}], None)
    assert "different working directories" in str(e.value)


def test_detect_repo_rejects_a_path_that_is_not_a_checkout(exp, tmp_path):
    with pytest.raises(SystemExit) as e:
        exp.detect_repo([{"cwd": str(REPO)}], str(tmp_path))
    assert "not a FableComputer checkout" in str(e.value)


def test_detect_repo_accepts_a_single_working_directory(exp):
    assert exp.detect_repo([{"cwd": str(REPO)}], None) == str(REPO)


def test_tokenize_replaces_every_note_variant_without_nesting(exp):
    raw = " / ".join(exp.NOTE_VARIANTS) + f" in {REPO}"
    out = exp.tokenize(raw, str(REPO))
    assert out.count("{{PLATFORM_NOTE}}") == len(exp.NOTE_VARIANTS)
    assert out.count("{{REPO}}") == 1
    assert "{{{{" not in out


# --------------------------------------------------------------------------- install

def _install(inst, monkeypatch, home, system, argv):
    monkeypatch.setattr(inst.platform, "system", lambda: system)
    monkeypatch.setattr(pathlib.Path, "home", staticmethod(lambda: home))
    monkeypatch.setattr(sys, "argv", ["install_routines.py", *argv])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = inst.main()
    return rc, buf.getvalue()


@pytest.mark.parametrize("system,marker", [
    ("Darwin", "python3"), ("Linux", "python3"), ("Windows", "PYTHONIOENCODING"),
])
def test_install_resolves_every_placeholder_for_each_os(inst, monkeypatch, tmp_path,
                                                        system, marker):
    rc, _ = _install(inst, monkeypatch, tmp_path, system, ["--repo", str(REPO)])
    assert rc == 0
    written = sorted(p.parent.name for p in (tmp_path / ".claude/scheduled-tasks").glob("*/SKILL.md"))
    assert written == sorted(r["id"] for r in ROUTINES if r["enabled"])
    for skill in (tmp_path / ".claude/scheduled-tasks").glob("*/SKILL.md"):
        text = skill.read_text(encoding="utf-8")
        assert "{{" not in text, f"{skill.parent.name} still has a placeholder"
        assert str(REPO) in text
        assert marker in text
        assert skill.read_bytes().count(b"\r\n") == 0


def test_install_skips_disabled_routines_unless_asked(inst_disabled, monkeypatch, tmp_path):
    inst, tid = inst_disabled
    home = tmp_path / "default"
    home.mkdir()
    _install(inst, monkeypatch, home, "Darwin", ["--repo", str(REPO)])
    assert not (home / ".claude/scheduled-tasks" / tid).exists()

    other = tmp_path / "with-disabled"
    other.mkdir()
    _install(inst, monkeypatch, other, "Darwin", ["--repo", str(REPO), "--include-disabled"])
    assert (other / ".claude/scheduled-tasks" / tid / "SKILL.md").exists()


def test_install_refuses_a_repo_that_is_not_a_checkout(inst, monkeypatch, tmp_path):
    rc, _ = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(tmp_path)])
    assert rc == 2
    assert not (tmp_path / ".claude").exists()


def test_paste_block_carries_the_display_names(inst, monkeypatch, tmp_path):
    """Path A cannot set a display name through the creation tool, so the block must still
    surface the value — as something to set in the app afterwards."""
    _, out = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO)])
    assert MAC_NOTE in out and str(REPO) in out
    for r in ROUTINES:
        if r["enabled"] and r["displayName"]:
            assert r["displayName"] in out, r["id"]
    assert "Edit form" in out, "the block must say where a display name actually gets set"


# --------------------------------------------------------------------------- --register

def _registry(home: pathlib.Path, system: str = "Darwin") -> pathlib.Path:
    root = {"Darwin": "Library/Application Support/Claude/claude-code-sessions",
            "Linux": ".config/Claude/claude-code-sessions",
            "Windows": "AppData/Roaming/Claude/claude-code-sessions"}[system]
    reg = home / root / "session" / "sub" / "scheduled-tasks.json"
    reg.parent.mkdir(parents=True)
    reg.write_text(json.dumps({"scheduledTasks": [
        {"id": "pre-existing", "cwd": "/somewhere", "enabled": True,
         "filePath": "/somewhere/SKILL.md", "createdAt": 1700000000000}],
        "recordedSkips": {}}, indent=2), encoding="utf-8")
    return reg


def test_register_writes_entries_the_app_can_render(inst, monkeypatch, tmp_path):
    reg = _registry(tmp_path)
    _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO), "--register"])
    data = json.loads(reg.read_text(encoding="utf-8"))
    by_id = {t["id"]: t for t in data["scheduledTasks"]}

    assert "pre-existing" in by_id, "an unrelated routine must survive the patch"
    assert data["recordedSkips"] == {}, "sibling registry keys must survive"

    for r in ROUTINES:
        if not r["enabled"]:
            assert r["id"] not in by_id
            continue
        entry = by_id[r["id"]]
        assert entry["cwd"] == str(REPO)
        assert entry["filePath"].endswith("SKILL.md")
        assert entry["enabled"] is True
        assert entry["useWorktree"] == r["useWorktree"]
        # the app stores createdAt as epoch MILLISECONDS, not an ISO string
        assert isinstance(entry["createdAt"], int) and entry["createdAt"] > 10**12
        if r["displayName"]:
            assert entry["displayName"] == r["displayName"]
        else:
            assert "displayName" not in entry
        if r["schedule"] == "manual":
            assert "cronExpression" not in entry and "fireAt" not in entry


def test_register_backs_up_before_patching(inst, monkeypatch, tmp_path):
    reg = _registry(tmp_path)
    original = reg.read_bytes()
    _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO), "--register"])
    backups = list(reg.parent.glob("*.bak-*"))
    assert len(backups) == 1
    assert backups[0].read_bytes() == original


def test_dry_run_writes_absolutely_nothing(inst, monkeypatch, tmp_path):
    reg = _registry(tmp_path)
    before = reg.read_bytes()
    rc, _ = _install(inst, monkeypatch, tmp_path, "Darwin",
                     ["--repo", str(REPO), "--register", "--dry-run"])
    assert rc == 0
    assert reg.read_bytes() == before
    assert not (tmp_path / ".claude").exists()
    assert not list(reg.parent.glob("*.bak-*"))


def test_register_without_a_registry_reports_instead_of_crashing(inst, monkeypatch, tmp_path):
    """A first-ever install has no registry; it must still write the prompts, explain, and
    exit non-zero so an unattended run does not read as success."""
    rc, out = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO), "--register"])
    assert rc == 1
    assert "needs exactly one registry file" in out
    assert (tmp_path / ".claude/scheduled-tasks").exists(), "prompts should still be installed"


def test_paste_block_never_asks_for_a_retired_schedule(inst_disabled, monkeypatch, tmp_path):
    """The creation tool has no `enabled` parameter, so "create with the cron then disable"
    would leave the schedule live in between. A retired routine must be requested with no
    schedule, and its old cron must not appear as something to create."""
    inst, tid = inst_disabled
    _, out = _install(inst, monkeypatch, tmp_path, "Darwin",
                      ["--repo", str(REPO), "--include-disabled"])
    block = out.split(f"  - {tid}")[1].split("  - ")[0]
    assert "schedule: NONE" in block
    assert "must not be recreated" in block
    # the cron may be named as history, but never as the schedule to set
    assert "schedule: cron 0 7 * * *" not in block


def test_paste_block_does_not_ask_the_tool_for_fields_it_cannot_set(inst, monkeypatch, tmp_path):
    """create_scheduled_task takes taskId/prompt/description/schedule/notifyOnCompletion
    only. Asking it for a display name in the routine list would be asking for something
    impossible; the values belong in the Edit-form section instead."""
    _, out = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO)])
    request, _, edit_form = out.partition("cannot set")
    assert edit_form, "the block must name the fields the tool cannot set"
    for r in ROUTINES:
        if r["enabled"] and r["displayName"]:
            assert r["displayName"] not in request, \
                f"{r['id']}'s display name is inside the tool request"
            assert r["displayName"] in edit_form, r["id"]


# ------------------------------------------------------- install: a broken manifest entry

@pytest.fixture
def inst_sandbox(inst, tmp_path, monkeypatch):
    """The installer with its manifest/prompts redirected, so entries can be corrupted."""
    prompts = tmp_path / "src-prompts"
    prompts.mkdir()
    for p in (RD / "prompts").glob("*.md"):
        (prompts / p.name).write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
    manifest = tmp_path / "routines.json"
    manifest.write_text(json.dumps(MANIFEST, indent=2), encoding="utf-8")
    monkeypatch.setattr(inst, "PROMPTS", prompts)
    monkeypatch.setattr(inst, "MANIFEST", manifest)
    return inst, prompts, manifest


def test_a_routine_with_no_prompt_file_is_neither_installed_nor_registered(
        inst_sandbox, monkeypatch, tmp_path):
    inst, prompts, _ = inst_sandbox
    victim = next(r["id"] for r in ROUTINES if r["enabled"])
    (prompts / f"{victim}.md").unlink()
    home = tmp_path / "home"
    home.mkdir()
    reg = _registry(home)

    rc, out = _install(inst, monkeypatch, home, "Darwin", ["--repo", str(REPO), "--register"])
    assert rc == 1, "an incomplete install must not report success"
    assert not (home / ".claude/scheduled-tasks" / victim).exists()
    registered = {t["id"] for t in json.loads(reg.read_text(encoding="utf-8"))["scheduledTasks"]}
    assert victim not in registered, "filePath would point at a SKILL.md that was never written"
    assert victim not in out.split("=" * 78)[-1], "it must not appear in the paste-in block"


def test_a_literal_working_directory_in_the_manifest_is_honoured(
        inst_sandbox, monkeypatch, tmp_path):
    """The manifest can record a routine that deliberately runs outside this checkout."""
    inst, _, manifest = inst_sandbox
    data = json.loads(manifest.read_text(encoding="utf-8"))
    target = next(r for r in data["routines"] if r["enabled"])
    elsewhere = str(tmp_path / "other-project")
    target["cwd"] = elsewhere
    manifest.write_text(json.dumps(data, indent=2), encoding="utf-8")
    home = tmp_path / "home2"
    home.mkdir()
    reg = _registry(home)

    _install(inst, monkeypatch, home, "Darwin", ["--repo", str(REPO), "--register"])
    entry = {t["id"]: t for t in json.loads(reg.read_text(encoding="utf-8"))["scheduledTasks"]}
    assert entry[target["id"]]["cwd"] == elsewhere


# --------------------------------------------------------------- export: never lose work

@pytest.fixture
def exp_sandbox(exp, tmp_path, monkeypatch):
    """The export module writing into tmp_path instead of the repository."""
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    manifest = tmp_path / "routines.json"
    monkeypatch.setattr(exp, "PROMPTS", prompts)
    monkeypatch.setattr(exp, "MANIFEST", manifest)
    return exp, prompts, manifest


def _seed(manifest: pathlib.Path, prompts: pathlib.Path, ids, note="n"):
    manifest.write_text(json.dumps({
        "note": note, "exported_from": "Windows",
        "routines": [{"id": i, "displayName": "", "description": f"d {i}",
                      "schedule": "manual", "enabled": True, "useWorktree": False,
                      "cwd": "{{REPO}}"} for i in ids],
    }, indent=2), encoding="utf-8")
    for i in ids:
        (prompts / f"{i}.md").write_text(f"exported body of {i} in {{{{REPO}}}} {{{{PLATFORM_NOTE}}}}\n",
                                         encoding="utf-8")


def _live_task(home: pathlib.Path, tid: str, repo: str, exists=True, **kw):
    skill = home / ".claude" / "scheduled-tasks" / tid / "SKILL.md"
    if exists:
        skill.parent.mkdir(parents=True, exist_ok=True)
        skill.write_text(f"---\nname: {tid}\ndescription: live {tid}\n---\n\nlive body {tid}\n",
                         encoding="utf-8")
    task = {"id": tid, "cwd": repo, "enabled": True, "filePath": str(skill)}
    task.update(kw)
    return task


def _export(exp, monkeypatch, tasks, argv=()):
    monkeypatch.setattr(exp, "load_registry", lambda: list(tasks))
    monkeypatch.setattr(sys, "argv", ["export_routines.py", "--repo", str(REPO), *argv])
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = exp.main()
    return rc, buf.getvalue()


def test_an_unreadable_skill_never_deletes_its_exported_prompt(exp_sandbox, monkeypatch, tmp_path):
    """The failure mode: SKILL.md cannot be read, so the routine is skipped — and the prune
    step then deletes the committed copy, which is the only remaining copy."""
    exp, prompts, manifest = exp_sandbox
    _seed(manifest, prompts, ["keeper"])
    home = tmp_path / "home"
    rc, _ = _export(exp, monkeypatch, [_live_task(home, "keeper", str(REPO), exists=False)])

    assert (prompts / "keeper.md").exists(), "the exported prompt was destroyed"
    assert [r["id"] for r in json.loads(manifest.read_text(encoding="utf-8"))["routines"]] == ["keeper"]
    assert rc == 1, "an incomplete export must not report success"


def test_an_unreadable_skill_is_reported_not_raised(exp_sandbox, monkeypatch, tmp_path):
    """Present but unreadable — locked by the app, or a stale filePath pointing at a
    directory — must be reported like any other gap, not end the run in a traceback."""
    exp, prompts, manifest = exp_sandbox
    _seed(manifest, prompts, ["keeper"])
    blocked = tmp_path / "not-a-file"
    blocked.mkdir()
    task = {"id": "keeper", "cwd": str(REPO), "enabled": True, "filePath": str(blocked)}

    rc, out = _export(exp, monkeypatch, [task])          # must not raise
    assert rc == 1
    assert (prompts / "keeper.md").exists()
    assert [r["id"] for r in json.loads(manifest.read_text(encoding="utf-8"))["routines"]] == ["keeper"]


def test_exporting_from_a_second_machine_carries_absent_routines_forward(
        exp_sandbox, monkeypatch, tmp_path):
    """The Mac never installed the retired cron routine; exporting there must not drop it."""
    exp, prompts, manifest = exp_sandbox
    _seed(manifest, prompts, ["here", "only-on-the-other-machine"])
    home = tmp_path / "home"
    rc, out = _export(exp, monkeypatch, [_live_task(home, "here", str(REPO))])

    assert rc == 0
    ids = [r["id"] for r in json.loads(manifest.read_text(encoding="utf-8"))["routines"]]
    assert ids == ["here", "only-on-the-other-machine"]
    assert (prompts / "only-on-the-other-machine.md").exists()
    assert "carried forward" in out or "not registered on this machine" in out


def test_prune_drops_routines_this_machine_does_not_have(exp_sandbox, monkeypatch, tmp_path):
    exp, prompts, manifest = exp_sandbox
    _seed(manifest, prompts, ["here", "deleted-in-the-app"])
    home = tmp_path / "home"
    rc, _ = _export(exp, monkeypatch, [_live_task(home, "here", str(REPO))], ["--prune"])

    assert rc == 0
    ids = [r["id"] for r in json.loads(manifest.read_text(encoding="utf-8"))["routines"]]
    assert ids == ["here"]
    assert not (prompts / "deleted-in-the-app.md").exists()


def test_export_does_not_delete_files_it_never_generated(exp_sandbox, monkeypatch, tmp_path):
    exp, prompts, manifest = exp_sandbox
    _seed(manifest, prompts, ["here"])
    stray = prompts / "NOTES.md"
    stray.write_text("hand-written, not an export product\n", encoding="utf-8")
    home = tmp_path / "home"
    _export(exp, monkeypatch, [_live_task(home, "here", str(REPO))], ["--prune"])
    assert stray.exists(), "the export deleted a file that was not its own"


def test_export_ignores_routines_belonging_to_other_checkouts(exp_sandbox, monkeypatch, tmp_path):
    exp, prompts, manifest = exp_sandbox
    _seed(manifest, prompts, [])
    home = tmp_path / "home"
    other = str(tmp_path / "some-other-project")
    rc, out = _export(exp, monkeypatch, [
        _live_task(home, "ours", str(REPO)),
        _live_task(home, "theirs", other, cwd=other),
    ])
    assert rc == 0
    ids = [r["id"] for r in json.loads(manifest.read_text(encoding="utf-8"))["routines"]]
    assert ids == ["ours"], "another project's routine was committed into this repo"
    assert "not this checkout" in out


def test_check_notices_a_change_outside_the_routines_array(exp_sandbox, monkeypatch, tmp_path):
    exp, prompts, manifest = exp_sandbox
    home = tmp_path / "home"
    tasks = [_live_task(home, "here", str(REPO))]
    _export(exp, monkeypatch, tasks)                       # write a correct export
    assert _export(exp, monkeypatch, tasks, ["--check"])[0] == 0

    data = json.loads(manifest.read_text(encoding="utf-8"))
    data["note"] = "something else entirely"
    manifest.write_text(json.dumps(data, indent=2), encoding="utf-8")
    assert _export(exp, monkeypatch, tasks, ["--check"])[0] == 1


def test_detect_repo_treats_two_spellings_of_one_path_as_one(exp):
    variants = [{"cwd": str(REPO)}, {"cwd": str(REPO) + os.sep}]
    assert exp.detect_repo(variants, None) in {v["cwd"] for v in variants}


def test_load_registry_collapses_a_routine_registered_twice(exp, monkeypatch, tmp_path):
    files = []
    for n in ("a", "b"):
        f = tmp_path / f"{n}.json"
        f.write_text(json.dumps({"scheduledTasks": [
            {"id": "same", "cwd": f"/{n}", "enabled": True}]}), encoding="utf-8")
        files.append(f)
    monkeypatch.setattr(exp, "registry_paths", lambda: files)
    tasks = exp.load_registry()
    assert [t["id"] for t in tasks] == ["same"]
