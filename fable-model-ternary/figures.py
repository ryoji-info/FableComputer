# -*- coding: utf-8 -*-
"""Figures T1-T5 of The Fable Computer, Part III.

    python figures.py            # writes figures/figT1.png ... figT5.png

Every plotted number is either computed here from the released chains (the booking
curves of Figure T3) or transcribed from the reference outputs of the two design
listings in this folder (digital_lane_bonsai.out, ternary_qmac_design.out) and of
variants.py (variants.out); the source section is named beside each number.
"""
import math
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import variants as V                                   # noqa: E402  (imports the released chains)
import numpy as np                                     # noqa: E402
import matplotlib                                      # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                        # noqa: E402
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch   # noqa: E402
from matplotlib.ticker import FuncFormatter                     # noqa: E402
THOUSANDS = FuncFormatter(lambda v, _: f"{v:,.0f}")

OUT = os.path.join(HERE, "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8.5, "axes.titlesize": 9.5,
                     "axes.labelsize": 9, "legend.fontsize": 7.5, "figure.dpi": 110})
C = {"A0": "#1f77b4", "A1": "#2ca02c", "A2": "#ff7f0e", "A3": "#d62728", "B": "#9467bd",
     "REF": "#d62728", "CONS": "#ff7f0e", "PERM": "#2ca02c", "grey": "#777777"}


def box(ax, x, y, w, h, text, fc="#f3f3f3", ec="#444444", fs=8, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02", fc=fc, ec=ec, lw=1))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs,
            fontweight="bold" if bold else "normal", wrap=True)


def arrow(ax, x0, y0, x1, y1, text=None, fs=7):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=12, lw=1, color="#333333"))
    if text:
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.03, text, ha="center", va="bottom", fontsize=fs, color="#333333")


# ---------------------------------------------------------------- Figure T1: the system partition (Section 4.1)
fig = plt.figure(figsize=(7.2, 3.5))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def tbox(x, y, text, fc, fs=7.4):
    return ax.text(x, y, text, ha="center", va="center", fontsize=fs, linespacing=1.35,
                   bbox=dict(boxstyle="round,pad=0.7,rounding_size=0.4", fc=fc, ec="#444444", lw=1))


YB = 0.66
t_mem = tbox(0.125, YB, "DRAM / HBM\n\nternary weights,\nPTQ1_0 packing:\n5.67 GB streamed\nper token\n\nKV cache, GDN state", "#e8eef7")
t_host = tbox(0.50, YB, "CMOS host (perimeter)\n\nunpack trits to (p, n) planes\nHadamard rotation;\nQ8_0 of activations\n"
              "attention, GDN recurrence,\nnorms, vision tower, LM-head\nsoftmax; \u00d7 FP16 scales; accumulate", "#eef5e8")
t_fab = tbox(0.875, YB, "Fabric: L digital lanes\n\none 32-wide block per\n14.5-ps slot (69 GHz)\nselect stage, 236-adder\n"
             "Wallace tree, 12-bit adder\n\nno storage on the fabric", "#fbeeee")
fig.canvas.draw()
inv = ax.transAxes.inverted()


def edges(t):
    bb = t.get_bbox_patch().get_window_extent(fig.canvas.get_renderer())
    (x0, y0), (x1, y1) = inv.transform([[bb.x0, bb.y0], [bb.x1, bb.y1]])
    return x0, x1, y0, y1


m0, m1, _, _ = edges(t_mem)
h0, h1, hy0, hy1 = edges(t_host)
f0, f1, _, _ = edges(t_fab)


def harrow(x0, x1, y, label_above, label_below=None):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=11, lw=1, color="#333333",
                                 shrinkA=0, shrinkB=0))
    xm = (x0 + x1) / 2
    ax.text(xm, y + 0.025, label_above, ha="center", va="bottom", fontsize=7)
    if label_below:
        ax.text(xm, y - 0.025, label_below, ha="center", va="top", fontsize=6.2, color="#555555")


harrow(m1 + 0.004, h0 - 0.004, YB, "weights", "bandwidth-\nbound")
harrow(h1 + 0.004, f0 - 0.004, hy1 - 0.065, "launch", "384\u2013704 lines")
harrow(f0 - 0.004, h1 + 0.004, hy0 + 0.075, "readout", "26\u201391 lines")
ax.text(0.5, hy0 - 0.035, "every launch and readout line runs at 69 Gb/s, one bit per slot; the fabric holds nothing between slots",
        ha="center", va="top", fontsize=6.6, color="#555555")
ax.text(0.03, hy0 - 0.13, "What sets the speed (in-model, Section 4.6)", fontsize=8.2, fontweight="bold", va="top")
ax.text(0.03, hy0 - 0.195, "\u2022 tokens per second = memory bandwidth \u00f7 5.67 GB: 88, 176, 529 tok/s at 0.5, 1, 3 TB/s\n"
        "\u2022 one lane = 32 MACs per slot at 69 GHz = 86 tok/s of the 25.6 G MACs per token; 2, 3, 7 lanes keep pace\n"
        "\u2022 the fabric adds area and energy, not speed: 17 k to 62 k cells, about 1.7 mm\u00b2 at most, 0.13 to 0.64 W at 300 K\n"
        "\u2022 the host scales 800 M block sums per token (1.27 TFLOP/s at 529 tok/s) and launches 27 to 49 Tb/s of operands",
        fontsize=7.4, va="top", linespacing=1.6)
fig.savefig(os.path.join(OUT, "figT1.png"), dpi=220, bbox_inches="tight")
plt.close(fig)
try:                                                   # trim the blank band above the boxes
    from PIL import Image, ImageChops
    im = Image.open(os.path.join(OUT, "figT1.png")).convert("RGB")
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        pad = 18
        im.crop((max(bbox[0] - pad, 0), max(bbox[1] - pad, 0), min(bbox[2] + pad, im.width),
                 min(bbox[3] + pad, im.height))).save(os.path.join(OUT, "figT1.png"))
except ImportError:
    pass

# ---------------------------------------------------------------- Figure T2: the lane (Sections 4.2-4.3, 6.4)
ref = V.lane()
cols = ref["per_column"]
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.1))
ax = axs[0]
xs = sorted(cols)
groups = [((0,), "#ff7f0e", "analog-eligible at 4, 77 and 300 K (column 0)"),
          ((1, 2), "#d62728", "analog-eligible at 4 and 77 K (columns 1\u20132)"),
          ((3, 4, 5, 6), "#1f77b4", "analog-eligible at 4 K, not at 77 K (columns 3\u20136)"),
          ((7, 8, 9, 10), "#bbbbbb", "digital at every temperature (columns 7\u201310)")]
# eligibility b* = 6 / 2 / 0 at 4 / 77 / 300 K: ternary_qmac_design.py \u00a75, REF, Student-t
for cs, col, lab in groups:
    ax.bar(list(cs), [cols[c] for c in cs], color=col, edgecolor="#444444", label=lab)
ax.set_xlabel("bit column of the 32-wide block sum")
ax.set_ylabel("3:2 counters in the column")
ax.set_title("(A) Wallace tree: 236 counters, 8 stages")
ax.set_ylim(0, 52)
ax.legend(loc="upper right", fontsize=6.2)
ax = axs[1]
segs = [("select stage\n(incl. 32 sign NOT)", ref["sel_cells"], "#1f77b4"), ("weight fan-out", ref["fan_cells"], "#2ca02c"),
        ("248 full adders \u00d7 15", ref["tree_cells"], "#bbbbbb"), ("balancing buffers", 2616, "#ff7f0e"),
        ("re-sync stations", 393, "#9467bd")]
for row, (label, upto) in enumerate((("logic only", 3), ("timing-closed", 5))):
    left = 0
    for name, n, col in segs[:upto]:
        ax.barh(row, n, left=left, height=0.55, color=col, edgecolor="#444444",
                label=name if row == 1 else None)
        if n >= 700:
            ax.text(left + n / 2, row, f"{n:,d}", ha="center", va="center", fontsize=7,
                    color="white" if col != "#bbbbbb" else "#222222")
        else:
            ax.text(left + n / 2, row + 0.36, f"{n:,d}", ha="center", va="bottom", fontsize=6, color="#333333")
        left += n
    ax.text(left + 120, row, f"{left:,d}", ha="left", va="center", fontsize=8, fontweight="bold")
ax.set_yticks([0, 1])
ax.set_yticklabels(["logic\nonly", "timing-\nclosed"])
ax.set_ylim(-0.6, 1.6)
ax.set_xlim(0, 9600)
ax.set_xlabel("biased cells per lane (digital_lane_bonsai.py \u00a72)")
ax.set_title("(B) One lane: 8,169 cells (13.3-cell spacing)")
ax.xaxis.set_major_formatter(THOUSANDS)
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=3, fontsize=6.5, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figT2.png"), dpi=220, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- Figure T3: the bookings (Section 5)
Ts = np.linspace(4, 400, 160)
CEIL = 6.28e-9                               # digital_lane_bonsai.out §4, t4 yardstick
fig, axs = plt.subplots(1, 2, figsize=(7.2, 3.4))
ax = axs[0]
LS = {"A0": "-", "A1": "--", "A2": "-.", "A3": ":"}
LAB = {"A0": "A0 released (k = 8, full rail)", "A1": "A1 F = 2 softened k_eff, full rail",
       "A2": "A2 A1 + split swing (\u22123 dB)", "A3": "A3 A2 + one junction (\u22121 dB)"}
for key, name in (("A0", "A0 released (k 8, full rail)"), ("A1", "A1 F=2 k_eff, full rail"),
                  ("A2", "A2 A1 + split swing (-3 dB)"), ("A3", "A3 A2 + one junction (-1 dB)")):
    f = V.BOOK[name]
    ys = np.array([max(f(float(t)), 1e-40) for t in Ts])
    ax.semilogy(Ts, ys, color=C[key], ls=LS[key], lw=1.4, label=LAB[key])
# booking B: half-adder decode error from ternary_qmac_design.out §6, mapped onto the cell-BER axis by the
# 300 K emulation of digital_lane_bonsai.out §4 (SNR -4.0 dB at p_B = 5.48e-3 against the 42.5 dB yardstick)
TB = np.array([4, 20, 48, 77, 150, 300.0])
pB = np.array([2.106e-12, 1.901e-11, 1.752e-8, 1.212e-6, 1.644e-4, 5.479e-3])
ratio = CEIL * 10 ** ((42.5 + 4.0) / 10) / 5.479e-3
ax.semilogy(TB, pB * ratio, "o-", lw=0.8, color=C["B"], ms=4, label="B QMAC calculus on a half-adder decode (mapped)")
ax.axhline(CEIL, color="k", ls=":", lw=1, label="pass line 6.3×10⁻⁹ per decision")
for key, Tp, yy in (("A0", 394.5, 1e-33), ("A1", 292.0, 1e-33), ("A2", 144.4, 1e-33), ("A3", 114.1, 1e-21), ("B", 59.4, 1e-21)):
    ax.axvline(Tp, color=C[key], lw=0.9, ls="--", alpha=0.7)
    ax.text(Tp + (4 if Tp < 380 else -4), yy, f"{key}: {Tp:.0f} K", rotation=90, fontsize=6.3, color=C[key], va="bottom",
            ha=("left" if Tp < 380 else "right"))
ax.set_ylim(1e-40, 1)
ax.set_xlim(4, 400)
ax.set_xlabel("temperature (K)")
ax.set_ylabel("error per cell decision")
ax.set_title("(A) Five bookings of one decision, vs temperature")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2, fontsize=6.3, frameon=False)
ax = axs[1]
names = ["A0", "A1", "A2", "A3", "B"]
snr300 = [64.9, 40.6, 5.0, -2.5, -4.0]        # digital_lane_bonsai.out §4, t4
snr353 = [50.9, 30.1, -0.4, -6.9, -6.7]
x = np.arange(5)
ax.bar(x - 0.18, snr300, 0.36, color=[C[n] for n in names], edgecolor="#444444", label="300 K")
ax.bar(x + 0.18, snr353, 0.36, color=[C[n] for n in names], edgecolor="#444444", alpha=0.45, label="353 K")
ax.axhline(42.5, color="k", ls=":", lw=1)
ax.text(4.4, 44, "pass line 42.5 dB (Student-t)", fontsize=7, ha="right")
ax.axhline(0, color="#999999", lw=0.6)
ax.set_xticks(x)
ax.set_xticklabels(names)
ax.set_ylabel("lane digital-error SNR (dB)")
ax.set_title("(B) The lane's own error at the warm band")
ax.legend(loc="upper right")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "figT3.png"), dpi=220, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- Figure T4: the analog counter tree (Section 6)
T6 = np.array([4, 20, 48, 77, 150, 300.0])
QFA = {"REF": [1.302e-5, 3.917e-5, 8.801e-4, 5.016e-3, 3.299e-2, 1.476e-1],      # ternary_qmac_design.out §4
       "CONS": [4.010e-4, 9.554e-4, 9.318e-3, 3.034e-2, 1.031e-1, 3.213e-1],
       "PERM": [4.058e-13, 2.467e-11, 4.059e-7, 3.529e-5, 2.391e-3, 4.080e-2]}
NQFA = {"REF": [184, 154, 94, 65, 38, 15], "CONS": [94, 94, 38, 38, 15, 0], "PERM": [236, 236, 236, 154, 65, 15]}
fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.7))
ax = axs[0]
for k in ("REF", "CONS", "PERM"):
    ax.semilogy(T6, QFA[k], "o-", ms=3.5, color=C[k], label=k)
ax.axhline(3e-5, color="k", ls=":", lw=0.8)
ax.text(295, 1.1e-5, "TG1 pass ≤ 3×10⁻⁵", fontsize=6.5, va="top", ha="right")
ax.set_xlabel("temperature (K)")
ax.set_ylabel("QFA-3 symbol error")
ax.set_title("(A) QFA-3 symbol error")
ax.legend(fontsize=7)
ax = axs[1]
for k in ("REF", "CONS", "PERM"):
    ax.plot(T6, NQFA[k], "o-", ms=3.5, color=C[k], label=k)
ax.axhline(236, color="#999999", lw=0.6)
ax.legend(fontsize=7)
ax.set_xlabel("temperature (K)")
ax.set_ylabel("analog-eligible counters (of 236)")
ax.set_title("(B) Eligible counters at 41 dB")
ax.set_ylim(0, 250)
ax = axs[2]
eta = np.linspace(0.05, 1.0, 200)
Wc = (300 - 77) / 77
r = 0.125                                            # Joule model, ternary_qmac_design.out §6
for name, cr, col, ls, lw in (("77 K hybrid (65 analog)", 1 - 0.038, "#d62728", "-", 2.2), ("77 K all-digital", 1.0, "#1f77b4", "--", 1.2)):
    ax.plot(100 * eta, cr * r * (1 + Wc / eta), color=col, ls=ls, lw=lw, label=name)
ax.axhline(1.0, color="k", ls=":", lw=0.8)
ax.text(98, 1.08, "break-even\nvs 300 K", fontsize=6.5, ha="right", va="bottom")
ax.set_xlabel("cooler efficiency (% of Carnot)")
ax.set_ylabel("wall-plug power / warm lane")
ax.set_title("(C) Cooling decides")
ax.set_ylim(0, 4)
ax.legend(fontsize=6.5, loc="upper right")
fig.tight_layout(w_pad=1.5)
fig.savefig(os.path.join(OUT, "figT4.png"), dpi=220, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------- Figure T5: system scale and the levers (Sections 4.6, 8)
fig, axs = plt.subplots(1, 2, figsize=(7.2, 2.8))
ax = axs[0]
bw = np.array([0.5, 1.0, 3.0])
tps = bw * 1e12 / 5.669e9
lanes = np.ceil(tps / 86.26)
ax.plot(bw, tps, "o-", color="#1f77b4", label="tokens/s (memory-bound)")
for b_, t_, l_ in zip(bw, tps, lanes):
    ax.annotate(f"{int(l_)} lanes", (b_, t_), textcoords="offset points", xytext=((10, -4) if b_ < 2 else (-6, 6)), ha=("left" if b_ < 2 else "right"),
                va=("center" if b_ < 2 else "bottom"), fontsize=7.5)
ax.axhline(86.26, color="#999999", ls="--", lw=0.8)
ax.text(1.6, 95, "one lane at 69 GHz", fontsize=7)
ax.set_xlabel("weight-streaming bandwidth (TB/s)")
ax.set_ylabel("tokens per second, batch 1")
ax.set_title("(A) Speed is set by the memory; lanes keep pace")
ax.set_ylim(0, 660)
ax.legend(fontsize=7, loc="upper left")
ax = axs[1]
bits = [8, 6, 4, 2]
rec = [V.lane(b)["logic_cells"] for b in bits]
tfa = [V.lane(b, 32, "TFA [V2]")["logic_cells"] for b in bits]
tfa_c = [V.lane(b, 32, "TFA [V2]", False)["logic_cells"] for b in bits]
w = 0.26
x = np.arange(len(bits))
ax.bar(x - w, rec, w, color="#bbbbbb", edgecolor="#444444", label="record full adder (15 cells)")
ax.bar(x, tfa, w, color="#2ca02c", edgecolor="#444444", label="threshold full adder [V2] (5 cells)")
ax.bar(x + w, tfa_c, w, color="#1f77b4", edgecolor="#444444", label="[V2] + select in CMOS")
ax.set_xticks(x)
ax.set_xticklabels([f"{b}-bit" for b in bits])
ax.set_xlabel("activation precision (model-side lever)")
ax.set_ylabel("logic cells per lane (before timing)")
ax.set_title("(B) The two levers on lane size")
ax.yaxis.set_major_formatter(THOUSANDS)
ax.legend(fontsize=6.5)
fig.tight_layout(w_pad=3.0)
fig.savefig(os.path.join(OUT, "figT5.png"), dpi=220, bbox_inches="tight")
plt.close(fig)
print("wrote", ", ".join(f"figT{i}.png" for i in range(1, 6)), "to", OUT)
