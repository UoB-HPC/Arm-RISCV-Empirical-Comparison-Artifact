import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.collections import LineCollection
import matplotlib.patches as mpatches
import matplotlib.lines as mlines


colors = [
    "#E69F00",
    "#56B4E9",
    "#009E73",
    "#0072B2",
    "#F0E442",
    "#D55E00",
    "#CC79A7",
    "#8274EC",
    "#8A2817",
    "#8C3971",
]

line_data_arm = [[],[],[],[],[]]
line_data_rv = [[],[],[],[],[]]

f = open(sys.argv[1])

for line in f:
    split = line.split(" ")
    data = list(map(float, split[1][:-2].split(",")))
    # print (data)
    if split[0].startswith("outSTREAMarm"):
        line_data_arm[0] = data
    if split[0].startswith("outCLarm"):
        line_data_arm[1] = data
    if split[0].startswith("outLBMarm"):
        line_data_arm[2] = data
    if split[0].startswith("outBUDEarm"):
        line_data_arm[3] = data
    if split[0].startswith("outSWEEParm"):
        line_data_arm[4] = data

    if split[0].startswith("outSTREAMrv"):
        line_data_rv[0] = data
    if split[0].startswith("outCLrv"):
        line_data_rv[1] = data
    if split[0].startswith("outLBMrv"):
        line_data_rv[2] = data
    if split[0].startswith("outBUDErv"):
        line_data_rv[3] = data
    if split[0].startswith("outSWEEPrv"):
        line_data_rv[4] = data

xs = [4, 16, 64, 200, 500, 1000, 2000]

def create_tuples():
    arm = []
    riscv = []
    for line in line_data_arm:
        arm.append(np.column_stack((xs, line)))
    for line in line_data_rv:
        riscv.append(np.column_stack((xs, line)))
    return (arm, riscv)


fig, ax = plt.subplots()

ax.grid(True, linestyle="--", zorder=1)

for idx, line in enumerate(line_data_arm):
    ax.plot(
        xs, line, color=colors[idx], marker="s", linewidth=2, markersize=10, zorder=2
    )

for idx, line in enumerate(line_data_rv):
    ax.plot(
        xs,
        line,
        color=colors[idx],
        linestyle="dashed",
        marker="v",
        linewidth=2,
        markersize=10,
        zorder=2,
    )

yticks = np.arange(0, 90, 10)

stream = mpatches.Patch(color=colors[0], label="STREAM")
cloverLeaf = mpatches.Patch(color=colors[1], label="CloverLeaf")
lbm = mpatches.Patch(color=colors[2], label="LBM")
miniBude = mpatches.Patch(color=colors[3], label="miniBUDE")
miniSweep = mpatches.Patch(color=colors[4], label="miniSweep")

legend1 = plt.legend(
    handles=[stream, cloverLeaf, lbm, miniBude, miniSweep], bbox_to_anchor=(0.04, 1), loc="upper left"
)

riscv_line = mlines.Line2D(
    [], [], marker="v", markersize=5, label="RISC-V", linestyle="dashed", color="black"
)
arm_line = mlines.Line2D([], [], marker="s", markersize=5, label="ARM", color="black")

legend2 = plt.legend(
    handles=[arm_line, riscv_line], bbox_to_anchor=(0.4, 1), loc="upper left"
)


ax.add_artist(legend1)
ax.add_artist(legend2)

ax.set_xlabel("Window Size", labelpad=12, size=12)
ax.set_ylabel("Mean ILP", labelpad=12, size=12)

ax.set_yticks(yticks)

plt.savefig('lineGraph.pdf', bbox_inches='tight')

# plt.show()
