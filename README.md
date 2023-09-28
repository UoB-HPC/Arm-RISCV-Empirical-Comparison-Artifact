# An Empirical Comparison of the RISC-V and AArch64 Instruction Sets Artifact

This repository contains the artifact for the paper titled "An Empirical Comparison of the RISC-V and AArch64 Instruction Sets" https://doi.org/10.1145/3624062.3624233. It contains the set of binaries, minimal source codes, and scripts used to produce the results of the paper.

## Directory Structure

Below is the directory structure of this repository.

MinimalSources contains directories for each benchmark used (except LBM). Each directory contains stripped-down versions of each benchmark's git repository, removing unnecessary language or programming model variations to only what is used in this set of experiments. There is a distinction between ISAs due to the differing inline assembly snippets used to mark the start and end of kernels. All other source code is the same.

PrecompiledBinaries contains the exact binaries used to produce the results of the study. These binaries are used by the buildAndRun script to reproduce the results.

```bash
├── buildAndRun.sh
├── extractCPInfo.py
├── extractKernelCountInfo.py
├── extractWindowCPInfo.py
├── grouped_stacked_bar.py
├── MinimalSources
│   ├── AArch64
│   │   ├── CloverLeaf
│   │   ├── compileAllBinaries.sh
│   │   ├── miniBUDE
│   │   ├── miniSweep
│   │   └── STREAM
│   └── RISCV
│       ├── CloverLeaf
│       ├── compileAllBinaries.sh
│       ├── miniBUDE
│       ├── miniSweep
│       └── STREAM
├── PrecompiledBinaries
├── produceLineGraph.py
└── README.md
```

## Reproducing Results

### Dependencies 

To run the ```buildAndRun.sh``` script, you will need: git, cmake, some C++17 compatible compiler, and Python 3 with the NumPy and Matplotlib packages. To build the benchmarks from source GCC 9.2 and 12.2 are needed targeting AArch64 and rv64g instruction sets.

### Building and Running

To reproduce the results of the paper, simply run the ```buildAndRun.sh``` script. This will git clone SimEng, checkout the relevant commits, build SimEng, run all the pre-compiled binaries, and redirect the output to text files under a newly created ```output``` directory. Python scripts are then used to extract the relevant information from this output and reproduce the graphs and table data saved under the ```results``` directory. This script has been successfully tested on Ubuntu 22.04.

## Compiling Benchmarks from Source

Each ISA directory under ```MinimalSources``` contains a ```compileAllBinaries.sh``` script. These are mostly the same. To use your own compiler, edit the first four variables. ```gccCompilers``` should be the path to your gcc (or any other compiler) executable. ```gccCompilerNames``` should contain a shortened acronym of each compiler in the same order as ```gccCompilers```; these will be used in the final binary name. ```fortranCompilers```, again in the same order, should be the paths to your fortran compiler executable. ```gXXCompilers``` follows the same pattern but for C++ compilers.

Running the script will compile all the benchmarks either through their scripts/Makefiles or directly. Binaries will be saved in a new folder named ```ARMbuilds``` or ```RVbuilds``` at the top level directory for that benchmark, e.g., ```STREAM/ARMbuilds/STREAM.arm.9.2```
