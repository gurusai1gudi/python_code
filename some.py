#!/usr/bin/env python3
"""
UIDAI Aadhaar Saturation – India State Heatmap
0 < 5 Years Age Band | May 2026 | Bengaluru Regional Office
"""
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import matplotlib.lines as mlines
import numpy as np
import pandas as pd
import math, warnings
from pathlib import Path

warnings.filterwarnings("ignore")
plt.rcParams['font.family'] = 'DejaVu Sans'

# ── DATA (from Image 2) ─────────────────────────────────────────────
DATA = {
    "Karnataka":  (3272163, 2205026, 67),
    "Tamil Nadu": (3695630, 1636926, 44),
    "Kerala":     (1325003,  470185, 35),
    "Puducherry": (  77596,   40712, 52),
    "Lakshadweep":(   4967,    2451, 49),
}
TOTAL = (8375359, 4355300, 52)

NAVY, ORANGE = "#0B2D6B", "#FF6B00"

# ── TRAFFIC-LIGHT SCALE ─────────────────────────────────────────────
BINS   = [0, 41, 51, 61, 101]
COLS   = ["#D32F2F", "#FDD835", "#FB8C00", "#2E7D32"]
LABELS = ["0 – 40%", "41 – 50%", "51 – 60%", "≥ 61%"]
NODATA = "#D0D0D0"

def color(v):
    if pd.isna(v): return NODATA
    for i in range(len(BINS)-1):
        if BINS[i] <= v < BINS[i+1]: return COLS[i]
    return NODATA

# ── AADHAAR LOGO ────────────────────────────────────────────────────
def aadhaar_logo(ax):
    ax.set_xlim(0,100); ax.set_ylim(0,100)
    ax.set_aspect("equal"); ax.axis("off")
    cx, cy, R = 50, 62, 26
    for r in np.linspace(R+9,R,7):
        ax.add_patch(Circle((cx,cy),r,color=ORANGE,alpha=0.05*(r-R+2),zorder=0))
    for i in range(12):
        a = math.radians(i*30)
        ax.plot([cx+(R-3)*math.cos(a), cx+(R+11)*math.cos(a)],
                [cy+(R-3)*math.sin(a), cy+(R+11)*math.sin(a)],
                color=ORANGE, lw=2.5, solid_capstyle="round", zorder=2)
    ax.add_patch(Circle((cx,cy), R, color=ORANGE, zorder=3))
    ax.add_patch(Circle((cx,cy), R*0.68, color="white", zorder=4))
    for r in [R*0.52, R*0.37, R*0.22]:
        ax.add_patch(Circle((cx,cy), r, fill=False, edgecolor=ORANGE, lw=1.5, zorder=5))
    ax.add_patch(Circle((cx,cy), R*0.09, color=ORANGE, zorder=6))
    ax.text(cx,20,"AADHAAR",ha="center",va="center",fontsize=11,
            fontweight="bold",color=NAVY,zorder=7)

# ── LOAD MAP ────────────────────────────────────────────────────────
gdf_all = gpd.read_file("/home/claude/karnataka_raw.geojson")
gdf = gdf_all.dissolve(by="NAME_1").reset_index().rename(columns={"NAME_1":"state"})
gdf = gdf.to_crs("EPSG:4326")

sat_df = pd.DataFrame([(k,v[2]) for k,v in DATA.items()],columns=["state","sat"])
gdf = gdf.merge(sat_df, on="state", how="left")
gdf["color"]    = gdf["sat"].apply(color)
gdf["has_data"] = gdf["sat"].notna()

# ── FIGURE ──────────────────────────────────────────────────────────
fig = plt.figure(figsize=(26, 19), facecolor="white")
ax  = fig.add_axes([0.00, 0.04, 0.70, 0.86])
ax_logo = fig.add_axes([0.80, 0.86, 0.15, 0.11])
ax.set_facecolor("#EBF3FA")
ax.set_axis_off()

# Draw grey states
gdf[~gdf["has_data"]].plot(ax=ax, color=NODATA, edgecolor="#BBBBBB", lw=0.5, zorder=1)

# Draw colored states
gdf[gdf["has_data"]].plot(ax=ax, color=gdf[gdf["has_data"]]["color"],
                           edgecolor="#111111", lw=1.6, zorder=2)

# Highlight glow for data states
gdf[gdf["has_data"]].plot(ax=ax, color="none",
                           edgecolor=ORANGE, lw=3.5, alpha=0.30, zorder=3)

sk = [pe.withStroke(linewidth=3.2, foreground="white")]

# ── LABELS: grey states ─────────────────────────────────────────────
for _, r in gdf[~gdf["has_data"]].iterrows():
    if r.geometry is None or r.geometry.is_empty: continue
    pt = r.geometry.centroid
    ax.text(pt.x, pt.y, r["state"], ha="center", va="center",
            fontsize=4.0, color="#888888",
            path_effects=[pe.withStroke(linewidth=1.5,foreground="white")], zorder=4)

# ── LABELS: data states ─────────────────────────────────────────────
NORMAL_LABELS = ["Karnataka","Tamil Nadu","Kerala"]
for _, r in gdf[gdf["has_data"] & gdf["state"].isin(NORMAL_LABELS)].iterrows():
    pt = r.geometry.centroid
    ax.annotate(f"{r['state']}\n{int(r['sat'])}%",
                xy=(pt.x, pt.y), ha="center", va="center",
                fontsize=11.5, fontweight="bold", color="#111",
                path_effects=sk, zorder=6, multialignment="center")

# ── CALLOUT BOXES for tiny UTs ──────────────────────────────────────
# We'll draw them as annotation boxes with arrows pointing to the state
CALLOUTS = {
    "Puducherry":   {"pt_xy":(79.80,11.90), "centroid":(79.0,11.93),  "sat":52},
    "Lakshadweep":  {"pt_xy":(71.20,12.20), "centroid":(72.94,10.45), "sat":49},
}
for state, cfg in CALLOUTS.items():
    tx, ty = cfg["pt_xy"]
    cx2, cy2 = cfg["centroid"]
    sat_val = cfg["sat"]
    c = color(sat_val)
    # Arrow from box to state centroid
    ax.annotate(
        f"{state}\n{sat_val}%",
        xy=(cx2, cy2), xytext=(tx, ty),
        ha="center", va="center",
        fontsize=10, fontweight="bold", color="#111",
        path_effects=sk,
        arrowprops=dict(arrowstyle="-|>", color="#333333",
                        lw=1.3, mutation_scale=12),
        bbox=dict(boxstyle="round,pad=0.4", facecolor=c,
                  edgecolor="#111111", lw=1.2, alpha=0.92),
        zorder=8,
    )

# ── TITLE ────────────────────────────────────────────────────────────
fig.text(0.355, 0.975,
         "0-5 Age Group Aadhaar Penetration  (May 2026)",
         ha="center", va="top", fontsize=27, fontweight="bold", color="black")
fig.text(0.355, 0.944,
         "India Map  –  Bengaluru Regional Office Coverage",
         ha="center", va="top", fontsize=15, fontweight="semibold", color=NAVY)
line = mlines.Line2D([0.02,0.69],[0.934,0.934],
                     transform=fig.transFigure, color=NAVY, lw=2.0, zorder=20)
fig.add_artist(line)

# ── LEGEND ───────────────────────────────────────────────────────────
lx, ly, bw, bh, gap = 0.722, 0.830, 0.048, 0.056, 0.009
for i,(c,lbl) in enumerate(zip(COLS, LABELS)):
    y = ly - i*(bh+gap)
    fig.add_artist(mpatches.FancyBboxPatch((lx,y),bw,bh,
        boxstyle="square,pad=0",transform=fig.transFigure,
        facecolor=c,edgecolor="#111",lw=1.1,clip_on=False,zorder=12))
    fig.text(lx+bw+0.011, y+bh/2, lbl,
             transform=fig.transFigure, va="center",
             fontsize=12.5, fontweight="bold", color="#111")

# No data swatch
yn = ly - len(COLS)*(bh+gap)
fig.add_artist(mpatches.FancyBboxPatch((lx,yn),bw,bh,
    boxstyle="square,pad=0",transform=fig.transFigure,
    facecolor=NODATA,edgecolor="#888",lw=1.0,clip_on=False,zorder=12))
fig.text(lx+bw+0.011, yn+bh/2, "No Data",
         transform=fig.transFigure, va="center",
         fontsize=12.5, color="#555")

n = len(COLS)+1
total_h = n*(bh+gap)+0.022
fig.add_artist(FancyBboxPatch((lx-0.010, ly-(n-1)*(bh+gap)-0.012),
    bw+0.120, total_h, boxstyle="round,pad=0.005",
    transform=fig.transFigure, facecolor="none",
    edgecolor="#333", lw=1.6, clip_on=False, zorder=11))

# ── DATA TABLE ───────────────────────────────────────────────────────
tx0 = 0.718
# Header
fig.add_artist(FancyBboxPatch((tx0, 0.320), 0.260, 0.035,
    boxstyle="square,pad=0", transform=fig.transFigure,
    facecolor=NAVY, edgecolor="none", clip_on=False, zorder=12))
fig.text(tx0+0.130, 0.3375,
         "Aadhaar Saturation in 0 < 5 Years Age band (May 2026)",
         ha="center", va="center", fontsize=7.8, fontweight="bold",
         color="white", transform=fig.transFigure, zorder=13)

# Column headers
cols_x = [tx0+0.004, tx0+0.085, tx0+0.152, tx0+0.218]
col_hdrs = ["State", "Pop (0-5Y)", "Aadhaar Assigned", "Sat %"]
fig.add_artist(FancyBboxPatch((tx0, 0.290), 0.260, 0.030,
    boxstyle="square,pad=0", transform=fig.transFigure,
    facecolor="#1A4A9B", edgecolor="none", clip_on=False, zorder=12))
for cx3, hdr in zip(cols_x, col_hdrs):
    fig.text(cx3, 0.305, hdr, ha="left", va="center",
             fontsize=7.2, fontweight="bold", color="white",
             transform=fig.transFigure, zorder=13)

rows = list(DATA.items())
row_h = 0.038
for i,(state,(pop,aadh,sat)) in enumerate(rows):
    y = 0.290 - (i+1)*row_h
    bg = "#F2F5FF" if i%2==0 else "white"
    fig.add_artist(FancyBboxPatch((tx0,y),0.260,row_h-0.002,
        boxstyle="square,pad=0", transform=fig.transFigure,
        facecolor=bg, edgecolor="#CCCCCC", lw=0.5, clip_on=False, zorder=10))
    # Color indicator
    ax2 = fig.add_axes([tx0+0.003, y+0.009, 0.013, 0.020])
    ax2.add_patch(Circle((0.5,0.5),0.40,color=color(sat),zorder=5))
    ax2.set_xlim(0,1); ax2.set_ylim(0,1); ax2.axis("off")
    # Text
    fig.text(tx0+0.021, y+row_h/2-0.001, state,
             ha="left",va="center",fontsize=7.5,fontweight="bold",
             color="#111",transform=fig.transFigure,zorder=11)
    fig.text(cols_x[1], y+row_h/2-0.001, f"{pop:,}",
             ha="left",va="center",fontsize=7.0,color="#333",
             transform=fig.transFigure,zorder=11)
    fig.text(cols_x[2], y+row_h/2-0.001, f"{aadh:,}",
             ha="left",va="center",fontsize=7.0,color="#333",
             transform=fig.transFigure,zorder=11)
    fig.text(cols_x[3], y+row_h/2-0.001, f"{sat}%",
             ha="left",va="center",fontsize=9.0,fontweight="bold",
             color=color(sat),transform=fig.transFigure,zorder=11)

# Total row
ty2 = 0.290-(len(rows)+1)*row_h
fig.add_artist(FancyBboxPatch((tx0,ty2),0.260,row_h-0.002,
    boxstyle="square,pad=0",transform=fig.transFigure,
    facecolor=NAVY,edgecolor="none",clip_on=False,zorder=12))
t_pop,t_aadh,t_sat = TOTAL
for cx3,txt in zip(cols_x,["TOTAL",f"{t_pop:,}",f"{t_aadh:,}",f"{t_sat}%"]):
    fig.text(cx3,ty2+row_h/2-0.001,txt,
             ha="left",va="center",fontsize=7.8,fontweight="bold",
             color="white",transform=fig.transFigure,zorder=13)

# ── LOGO & FOOTER ────────────────────────────────────────────────────
aadhaar_logo(ax_logo)
fig.text(0.355, 0.024,
         "Source: UIDAI  ·  Unique Identification Authority of India  ·  May 2026  ·  Bengaluru Regional Office",
         ha="center", va="bottom", fontsize=9.5, color="#555")

plt.savefig("/mnt/user-data/outputs/india_aadhaar_heatmap_v2.png",
            dpi=220, bbox_inches="tight", facecolor="white")
plt.close()
print("Done ✓")