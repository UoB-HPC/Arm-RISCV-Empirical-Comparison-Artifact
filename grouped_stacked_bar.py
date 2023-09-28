import ast
import sys

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

compilers = np.array(["GCC 9", "GCC 12"])

# font_path = "/home/rahat/Desktop/fonts/opentype/public/libertine/LinLibertine_DR.otf"
# font_prop = fm.FontProperties(fname=font_path)

plt.rcParams["hatch.color"] = "#464646"
plt.rcParams["hatch.linewidth"] = 0.5

row1_data = [
    {
        "name": "STREAM",
        "labels": np.array(
            [
                "Setup",
                "Copy",
                "Scale",
                "Add",
                "Triad",
                "Summary",
            ]
        ),
        "benchmarks": {
            "GCC 9.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
            "GCC 12.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
        },
    },
    {
        "name": "Minisweep",
        "labels": np.array(
            [
                "Setup",
                "Initialise Faces",
                "Solve",
                "Finalise",
            ]
        ),
        "benchmarks": {
            "GCC 9.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
            "GCC 12.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
        },
    },
    {
        "name": "miniBUDE",
        "labels": np.array(["Setup & Warm-Up", "Solve", "Validate"]),
        "benchmarks": {
            "GCC 9.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
            "GCC 12.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
        },
    },
]

row2_data = [
    {
        "name": "LBM",
        "labels": np.array(
            [
                "Initialise",
                "Solve",
                "File Write",
            ]
        ),
        "benchmarks": {
            "GCC 9.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
            "GCC 12.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
        },
    },
    {
        "name": "CloverLeaf",
        "labels": np.array(
            [
                "Initialise",
                "Print Timestep Results",
                "timestep",
                "PdV(TRUE)",
                "accelerate",
                "PdV(FALSE)",
                "flux_calc",
                "advection",
                "reset_field",
                "Field Summary",
            ]
        ),
        "benchmarks": {
            "GCC 9.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
            "GCC 12.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
        },
    },
    {
        "name": "miniBUDE",
        "labels": np.array(["Setup & Warm-Up", "Solve", "Validate"]),
        "benchmarks": {
            "GCC 9.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
            "GCC 12.2": {
                "ARM": np.array([]),
                "RISC-V": np.array([]),
            },
        },
    },
]

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


# Read in data

def insertIntoRowData(dictionary):
    dictionary["benchmarks"]["GCC 9.2"]["ARM"] = np.array(normalisedCountList[0])
    dictionary["benchmarks"]["GCC 9.2"]["RISC-V"] = np.array(normalisedCountList[2])
    dictionary["benchmarks"]["GCC 12.2"]["ARM"] = np.array(normalisedCountList[1])
    dictionary["benchmarks"]["GCC 12.2"]["RISC-V"] = np.array(normalisedCountList[3])


f = open(sys.argv[1])

atSection = False
for line in f:
    if not atSection:
        if line.startswith('Norm Arrays'):
            atSection = True
    else:
        split = line.split(':')
        workloadName = split[0]
        normalisedCountList = ast.literal_eval(split[1])

        if workloadName == 'STREAM':
            insertIntoRowData(row1_data[0])
        if workloadName == "sweep":
            insertIntoRowData(row1_data[1])
        if workloadName == "BUDE":
            insertIntoRowData(row1_data[2])
        if workloadName == "LBM":
            insertIntoRowData(row2_data[0])
        if workloadName == "clover":
            insertIntoRowData(row2_data[1])



x_axis = np.arange(len(compilers))

fig, (row1, row2) = plt.subplots(2, 3, sharey=True)
fig.tight_layout()

patterns = {"ARM": "\\\\", "RISC-V": "//."}


def make_graph(axes, row, rcount):
    width = 0.25
    multiplier = 0
    for r_idx, ax in enumerate(axes):
        if r_idx == rcount:
            break
        ax.grid(True, linestyle="--", zorder=1)

        rdata = row[r_idx]
        labels = rdata["labels"]
        label_len = len(labels)
        bname = rdata["name"]
        items = rdata["benchmarks"].items()

        bottom = np.zeros(len(labels))

        for compiler, isa_data in items:
            offset = 2.5 * width * multiplier
            count = 0
            delta = 0
            for isa, data in isa_data.items():
                bottom = 0
                for idx, weight in enumerate(data):
                    b = ax.bar(
                        x=(delta + offset + (width * count)),
                        height=weight,
                        width=width,
                        label=isa,
                        bottom=bottom,
                        color=colors[idx],
                        zorder=2,
                    )

                    if idx == label_len - 1:
                        ax.bar_label(
                            b, [("%s\n%s" % (isa, compiler))], size=7, weight="bold"
                        )

                    bottom += weight
                delta += 0.01
                count += 1
            multiplier += 1

        ax.set_xticks([])
        ax.set_yticks(
            [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]
        )
        # ax.set_title(bname, size=10, pad=40)
        ax.set_xlabel(bname)
        ax.legend(
            labels,
            bbox_to_anchor=(0, 1.02, 1, 0.2),
            loc="lower left",
            mode="expand",
            ncols=3,
            prop={"size": 7},
        )


make_graph(row1, row1_data, 3)
make_graph(row2, row2_data, 2)

row2[2].set_visible(False)
row2[1].legend(
    row2_data[1]["labels"],
    bbox_to_anchor=(1.04, 0.5),
    loc="center left",
    ncols=1,
    prop={"size": 7},
)

fig.supylabel("Normalised Instruction Count")

plt.savefig('barChart.pdf', bbox_inches='tight')
# plt.show()
