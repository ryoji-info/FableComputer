<img src="branding/boogie-sorbet-monogram.svg" alt="" width="72" align="right">

# Licensing

This repository contains three kinds of material, under three licenses. This
scheme was chosen once, deliberately, and the project commits to **never
tightening it**: material published under these terms stays under them.

| Material | License | File |
|---|---|---|
| Code (`fable-model-chain/`, `fable-model-quantum/`, and all future code) | [Apache License 2.0](LICENSE) | `LICENSE` |
| Manuscripts, documentation, and figures (`papers/`, `*.md`, generated figures) | [Creative Commons Attribution 4.0](LICENSE-docs) | `LICENSE-docs` |
| Hardware design files (none yet; declared in advance) | [CERN-OHL-S v2.0](https://ohwr.org/cern_ohl_s_v2.txt) | added with the first hardware files |

**Why these three:**

- **Apache-2.0** rather than MIT because its Section 3 grants every user an
  express patent license from every contributor and revokes it from anyone who
  sues over the code. For a physics project whose contributors may hold or
  file patents, that protection matters.
- **CC BY 4.0** is for prose and figures only. It grants no patent rights, so
  it is never applied to code or hardware designs here.
- **CERN-OHL-S** (strongly reciprocal) is declared now, before any hardware
  files exist, so that future fabric or half-adder design files cannot be
  forked closed. Anyone who manufactures from or modifies those files must
  publish their sources under the same terms.

**Defensive publication.** The project publishes everything — models, designs,
data, negative results — openly and citably (git tags, DOI snapshots, preprint
servers). This is a deliberate IP strategy: published work is prior art that
no one, including this project, can later enclose behind patents. Any
exception (a decision to file rather than publish) would require a recorded
governance decision before the material is released, and the default is
publish.

**Contributions.** By contributing, you agree your contribution is licensed
under the license covering the material you contribute to (inbound = outbound).
There is no CLA and no copyright assignment.
