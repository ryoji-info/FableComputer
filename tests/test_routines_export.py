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


def test_install_skips_disabled_routines_unless_asked(inst, monkeypatch, tmp_path):
    disabled = [r["id"] for r in ROUTINES if not r["enabled"]]
    if not disabled:
        pytest.skip("no disabled routine in the manifest")
    _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO)])
    assert not (tmp_path / ".claude/scheduled-tasks" / disabled[0]).exists()

    other = tmp_path / "with-disabled"
    other.mkdir()
    _install(inst, monkeypatch, other, "Darwin", ["--repo", str(REPO), "--include-disabled"])
    assert (other / ".claude/scheduled-tasks" / disabled[0] / "SKILL.md").exists()


def test_install_refuses_a_repo_that_is_not_a_checkout(inst, monkeypatch, tmp_path):
    rc, _ = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(tmp_path)])
    assert rc == 2
    assert not (tmp_path / ".claude").exists()


def test_paste_block_carries_the_display_names(inst, monkeypatch, tmp_path):
    """Path A (asking Claude Code) must be able to reproduce the app-side naming."""
    _, out = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO)])
    assert MAC_NOTE in out and str(REPO) in out
    for r in ROUTINES:
        if r["enabled"] and r["displayName"]:
            assert r["displayName"] in out, r["id"]


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
    """A first-ever install has no registry; it must still write the prompts and explain."""
    rc, out = _install(inst, monkeypatch, tmp_path, "Darwin", ["--repo", str(REPO), "--register"])
    assert rc == 0
    assert "needs exactly one registry file" in out
    assert (tmp_path / ".claude/scheduled-tasks").exists(), "prompts should still be installed"
