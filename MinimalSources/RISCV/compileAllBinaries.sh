#!/bin/bash
#Compile all benchmarks in this directory with all gccCompilers
clear

gccCompilers=(<path/to/RISC-V/gcc9.2> <path/to/RISC-V/gcc12.2>)  # Change this
gccCompilerNames=(9.2 12.2) # Change this
fortranCompilers=(<path/to/RISC-V/gfortran9.2> <path/to/RISC-V/gfortran12.2>) # Change this
gXXCompilers=(<path/to/RISC-V/g++9.2> <path/to/RISC-V/g++12.2>) # Change this
compilerIndex=0
ROOT_DIR=$PWD
echo ROOT_DIR = $ROOT_DIR
echo

ISAname=rv
buildDirName=RVbuilds
commonCompilerOptions="--static -mtune=sifive-7-series -march=rv64g"


#compileSTREAM: compilerCommand
compileSTREAM() {
  #print what you are doing
  # echo $1 -O $ROOT_DIR/STREAM/STREAM/stream.c -o stream $commonCompilerOptions

  mkdir $ROOT_DIR/STREAM/$buildDirName
  #compile
  $1 -O $ROOT_DIR/STREAM/STREAM/stream.c  -o $ROOT_DIR/STREAM/STREAM/stream $commonCompilerOptions
  #copy output
  cp $ROOT_DIR/STREAM/STREAM/stream $ROOT_DIR/STREAM/$buildDirName/STREAM.$ISAname.${gccCompilerNames[$compilerIndex]}
}

compileMiniBUDE() {
  cd $ROOT_DIR/miniBUDE/miniBUDE/openmp || exit
  mkdir $ROOT_DIR/miniBUDE/$buildDirName

  CC_GNU=$1 make COMPILER=GNU
  cp bude $ROOT_DIR/miniBUDE/$buildDirName/BUDE.$ISAname.${gccCompilerNames[$compilerIndex]}

  cd $ROOT_DIR || exit
}

compileCloverLeaf() {
  cd $ROOT_DIR/CloverLeaf/CloverLeaf/ || exit
  mkdir $ROOT_DIR/CloverLeaf/$buildDirName

  make clean
  C_MPI_COMPILER_GNU=$1 MPI_COMPILER_GNU=${fortranCompilers[$compilerIndex]}  make COMPILER=GNU
  cp clover_leaf $ROOT_DIR/CloverLeaf/$buildDirName/CL.$ISAname.${gccCompilerNames[$compilerIndex]}

  cd $ROOT_DIR || exit
}

compileMiniSweep() {
  rm -r $ROOT_DIR/miniSweep/${gccCompilerNames[$compilerIndex]}
  mkdir $ROOT_DIR/miniSweep/${gccCompilerNames[$compilerIndex]}
  cd $ROOT_DIR/miniSweep/${gccCompilerNames[$compilerIndex]} || exit
  mkdir $ROOT_DIR/miniSweep/$buildDirName

  BUILD=Release NM_VALUE=16 CC=$1 ../minisweep/scripts/cmake_serial.sh
  make
  cp sweep $ROOT_DIR/miniSweep/$buildDirName/SWEEP.$ISAname.${gccCompilerNames[$compilerIndex]}

  cd $ROOT_DIR || exit
}

for i in "${gccCompilers[@]}"; do
  compileSTREAM $i;
  compileMiniBUDE $i;
  compileCloverLeaf $i;
  compileMiniSweep $i;

  ((compilerIndex=compilerIndex+1));
done




