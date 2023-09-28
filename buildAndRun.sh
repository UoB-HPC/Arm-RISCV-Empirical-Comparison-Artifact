#!/bin/bash

#dependencies = git (w/github ssh keys set up), cmake, python 3.10, numpy

ROOT_DIR=$PWD
SIMENG_INSTALL_DIR=$ROOT_DIR/SimEngInstall
PRECOMPILED_BINS_DIR=$ROOT_DIR/PrecompiledBinaries
BIN_OUTPUT_DIR=$ROOT_DIR/output
RESULT_DIR=$ROOT_DIR/results
PROCESSORS ?= 4

#REMOVE ALL OLD OUTPUT FROM THE BEGINNING output and results

#FUNCTIONS

buildSimEng() {
  #cmake build simeng
  cmake -B build -S . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=$SIMENG_INSTALL_DIR
  cmake --build build -j $PROCESSORS

  #cmake install simeng
  cmake --build build --target install
}

#runAllBinaries config_directory binary_postfix output_dir
runAllBinaries() {
  RUN_SIMENG="$SIMENG_INSTALL_DIR/bin/simeng $1"
  cd "$PRECOMPILED_BINS_DIR" || exit

  # STREAM

  echo Starting STREAM
  for FILE in "$PRECOMPILED_BINS_DIR/STREAM.$2"*; do
    $RUN_SIMENG $FILE
  done >> $3/outSTREAM$2.txt 2>&1

  # CloverLeaf

  echo Starting CloverLeaf
  for FILE in "$PRECOMPILED_BINS_DIR/CL.$2"*; do
    $RUN_SIMENG $FILE
  done >> $3/outCL$2.txt 2>&1

  #LBM

  echo Starting LBM
  for FILE in "$PRECOMPILED_BINS_DIR/LBM.$2"*; do
    $RUN_SIMENG $FILE $PRECOMPILED_BINS_DIR/input_128x128.params $PRECOMPILED_BINS_DIR/obstacles_128x128.dat
  done >> $3/outLBM$2.txt 2>&1

  #miniBUDE

  echo Starting miniBUDE
  for FILE in "$PRECOMPILED_BINS_DIR/BUDE.$2"*; do
    $RUN_SIMENG $FILE  -n 64 -i 1 --deck $PRECOMPILED_BINS_DIR/bm1
  done >> $3/outBUDE$2.txt 2>&1

  #miniSweep

  echo Starting miniSweep
  for FILE in "$PRECOMPILED_BINS_DIR/SWEEP.$2"*; do
    $RUN_SIMENG $FILE  --ncell_x  8 --ncell_y 16 --ncell_z 32 --ne 1 --na 32
  done >> $3/outSWEEP$2.txt 2>&1

  cd "$ROOT_DIR/SimEng" || exit
}



windowSizes=( 4 16 64 200 500 1000 2000 )
offsets=( 0.0 0.5 )

#runBinariesWindow config_directory binary_postfix output_dir
runBinariesWindow(){
    RUN_SIMENG="$SIMENG_INSTALL_DIR/bin/simeng $1"
    cd "$PRECOMPILED_BINS_DIR" || exit

  for win in "${windowSizes[@]}" ; do
    for off in "${offsets[@]}"; do
      echo "Window size $win, offset $off"
      windowOff="$win $off"

      # STREAM

      echo Starting STREAM
      for FILE in "$PRECOMPILED_BINS_DIR/STREAM.$2.12"*; do
        $RUN_SIMENG $FILE $windowOff
      done >> $3/outSTREAM$2.txt 2>&1

      # CloverLeaf

      echo Starting CloverLeaf
      for FILE in "$PRECOMPILED_BINS_DIR/CL.$2.12"*; do
        $RUN_SIMENG $FILE $windowOff
      done >> $3/outCL$2.txt 2>&1

      #LBM

      echo Starting LBM
      for FILE in "$PRECOMPILED_BINS_DIR/LBM.$2.12"*; do
        $RUN_SIMENG $FILE $windowOff $PRECOMPILED_BINS_DIR/input_128x128.params $PRECOMPILED_BINS_DIR/obstacles_128x128.dat
      done >> $3/outLBM$2.txt 2>&1

      #miniBUDE

      echo Starting miniBUDE
      for FILE in "$PRECOMPILED_BINS_DIR/BUDE.$2.12"*; do
        $RUN_SIMENG $FILE $windowOff -n 64 -i 1 --deck $PRECOMPILED_BINS_DIR/bm1
      done >> $3/outBUDE$2.txt 2>&1

      #miniSweep

      echo Starting miniSweep
      for FILE in "$PRECOMPILED_BINS_DIR/SWEEP.$2.12"*; do
        $RUN_SIMENG $FILE $windowOff --ncell_x  8 --ncell_y 16 --ncell_z 32 --ne 1 --na 32
      done >> $3/outSWEEP$2.txt 2>&1

    done
  done

  cd "$ROOT_DIR/SimEng" || exit
}

#--START--

if [ ! -d "${BIN_OUTPUT_DIR}" ]; then
  mkdir $BIN_OUTPUT_DIR
fi

if [ ! -d "${RESULT_DIR}" ]; then
  mkdir $RESULT_DIR
fi

#Clone SimEng
if [ ! -d "${ROOT_DIR}/SimEng" ]; then
  git clone git@github.com:UoB-HPC/SimEng.git
fi

cd SimEng || exit

#--Kernel count--
echo KERNEL COUNT

#git checkout correct branch
git checkout bc9f65d

buildSimEng

rm -rf $BIN_OUTPUT_DIR/kernCount
mkdir $BIN_OUTPUT_DIR/kernCount

runAllBinaries $PRECOMPILED_BINS_DIR/RISCV.yaml rv $BIN_OUTPUT_DIR/kernCount
runAllBinaries $PRECOMPILED_BINS_DIR/AARCH64.yaml arm $BIN_OUTPUT_DIR/kernCount

python3 $ROOT_DIR/extractKernelCountInfo.py $BIN_OUTPUT_DIR/kernCount/ > $RESULT_DIR/kernelCounts.txt

cd $RESULT_DIR || exit
python3 $ROOT_DIR/grouped_stacked_bar.py $RESULT_DIR/kernelCounts.txt
cd $ROOT_DIR/SimEng || exit

#--Critical Path--

echo CRITICAL PATH

rm -rf $BIN_OUTPUT_DIR/basicCP
mkdir $BIN_OUTPUT_DIR/basicCP

#RISC-V

git checkout de225ef
buildSimEng

runAllBinaries $PRECOMPILED_BINS_DIR/RISCV.yaml rv $BIN_OUTPUT_DIR/basicCP

#AArch64

git checkout f9a7442
buildSimEng

runAllBinaries $PRECOMPILED_BINS_DIR/AARCH64.yaml arm $BIN_OUTPUT_DIR/basicCP

python3 $ROOT_DIR/extractCPInfo.py $BIN_OUTPUT_DIR/basicCP/ > $RESULT_DIR/basicCPResult.txt

#--Scaled Critical Path--

echo SCALED CRITICAL PATH

rm -rf $BIN_OUTPUT_DIR/scaledCP
mkdir $BIN_OUTPUT_DIR/scaledCP

git checkout a60f2ec # THIS MAY BE INCORRECT AND MAY ADD LOAD/STORE LATENCIES. Latencies are 1!!
buildSimEng

runAllBinaries $PRECOMPILED_BINS_DIR/RISCV.yaml rv $BIN_OUTPUT_DIR/scaledCP

#AArch64

git checkout eca29f0 # THIS MAY BE INCORRECT AND MAY ADD LOAD/STORE LATENCIES. Latencies are 1!!
buildSimEng

runAllBinaries $PRECOMPILED_BINS_DIR/AARCH64.yaml arm $BIN_OUTPUT_DIR/scaledCP

python3 $ROOT_DIR/extractCPInfo.py $BIN_OUTPUT_DIR/scaledCP/ > $RESULT_DIR/scaledCPResult.txt


#--Windowed Critical Path--

echo WINDOWED CRITICAL PATH

rm -rf $BIN_OUTPUT_DIR/windowedCP
mkdir $BIN_OUTPUT_DIR/windowedCP

#RISC-V
git checkout 37f9983
buildSimEng

runBinariesWindow $PRECOMPILED_BINS_DIR/RISCV.yaml rv $BIN_OUTPUT_DIR/windowedCP

#AArch64
git checkout 278107c
buildSimEng

runBinariesWindow $PRECOMPILED_BINS_DIR/AARCH64.yaml arm $BIN_OUTPUT_DIR/windowedCP

#Process raw data and find average ILP per window size
python3 $ROOT_DIR/extractWindowCPInfo.py $BIN_OUTPUT_DIR/windowedCP/ > $RESULT_DIR/windowAverages.txt

#Produce graph
cd $RESULT_DIR || exit

python3 $ROOT_DIR/produceLineGraph.py $RESULT_DIR/windowAverages.txt

#rm -rf SimEng
#rm -rf SimEngInstall
#rm -rf $BIN_OUTPUT_DIR
#rm -rf $RESULT_DIR
