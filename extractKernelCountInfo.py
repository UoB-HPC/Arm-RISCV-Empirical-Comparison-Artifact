import os
import sys

STREAMInstr = "Main,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,Start Copy,Start Scale,Start Add,Start MultAdd,End MultAdd,End".split(
    ",")
LBMInstr = "Start,Start Timesteps,End Timesteps,End".split(",")
BUDEInstr = "START, Start Fasten, End Fasten, End".split(",")
sweepInstr = "Start,Start Sweep,Loop over Octants,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,Loop Over Energy Groups,End Energy Groups Loop,End Octant Loop,End Sweep,END".split(
    ",")
cloverInstr = "Start,      Start Hydro,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,   Start timestep,   Start PdV True, Start Accelerate,  Start PdV False,  Start Flux Calc,  Start Advection,Start Reset Field,  END Reset Field,        End Hydro".split(
    ",")

STREAMCombined = [[], [], [], []]
STREAMarm9Total = 0

LBMCombined = [[], [], [], []]
LBMarm9Total = 0

BUDECombined = [[], [], [], []]
BUDEarm9Total = 0

sweepCombined = [[], [], [], []]
sweeparm9Total = 0

cloverCombined = [[], [], [], []]
cloverarm9Total = 0


# STREAMDict = {}
# LBMDict = {}
# BUDEDict = {}
# sweepDict = {}
# cloverDict = {}


# def calcLBM(data):
#     n = 0
#     previousName = "undef"
#     for datum in data:
#         if n > len(LBMInstr) - 1:
#             currentName = "undef"
#         else:
#             currentName = LBMInstr[n]
#
#         if (previousName, currentName) in LBMDict.keys():
#             LBMDict[(previousName, currentName)] += datum
#         else:
#             LBMDict[(previousName, currentName)] = datum
#
#         previousName = currentName
#         n += 1
#
#     print(LBMDict)
#     LBMDict.clear()


# def calcSTREAM(data):
#     n = 0
#     previousName = "undef"
#     for datum in data:
#         if n > len(STREAMInstr) - 1:
#             currentName = "undef"
#         else:
#             currentName = STREAMInstr[n]
#
#         if (previousName, currentName) in STREAMDict.keys():
#             STREAMDict[(previousName, currentName)] = int(STREAMDict[(previousName, currentName)]) + int(datum)
#         else:
#             STREAMDict[(previousName, currentName)] = datum
#
#         previousName = currentName
#         n += 1
#
#     print(STREAMDict)
#     STREAMDict.clear()


# def calcBUDE(data):
#     n = 0
#     previousName = "undef"
#     for datum in data:
#         if n > len(BUDEInstr) - 1:
#             currentName = "undef"
#         else:
#             currentName = BUDEInstr[n]
#
#         if (previousName, currentName) in BUDEDict.keys():
#             BUDEDict[(previousName, currentName)] += datum
#         else:
#             BUDEDict[(previousName, currentName)] = datum
#
#         previousName = currentName
#         n += 1
#
#     print(BUDEDict)
#     BUDEDict.clear()


# def calcsweep(data):
#     n = 0
#     previousName = "undef"
#     for datum in data:
#         if n > len(sweepInstr) - 1:
#             currentName = "undef"
#         else:
#             currentName = sweepInstr[n]
#
#         if (previousName, currentName) in sweepDict.keys():
#             sweepDict[(previousName, currentName)] = int(sweepDict[(previousName, currentName)]) + int(datum)
#         else:
#             sweepDict[(previousName, currentName)] = datum
#
#         previousName = currentName
#         n += 1
#
#     # Combine first loop with others
#     sweepDict[('End Energy Groups Loop', 'Loop Over Energy Groups')] = int(
#         sweepDict[('End Energy Groups Loop', 'Loop Over Energy Groups')]) + int(
#         sweepDict[('Loop over Octants', 'Loop Over Energy Groups')])
#     sweepDict.pop(('Loop over Octants', 'Loop Over Energy Groups'))
#
#     print(sweepDict)
#     sweepDict.clear()


# def calcclover(data):
#     n = 0
#     previousName = "undef"
#     for datum in data:
#         if n > len(cloverInstr) - 1:
#             currentName = "undef"
#         else:
#             currentName = cloverInstr[n]
#
#         if (previousName, currentName) in cloverDict.keys():
#             cloverDict[(previousName, currentName)] = int(cloverDict[(previousName, currentName)]) + int(datum)
#         else:
#             cloverDict[(previousName, currentName)] = datum
#
#         previousName = currentName
#         n += 1
#
#     # Add small preloop count to interloop count
#     cloverDict[('  END Reset Field', '   Start timestep')] = int(
#         cloverDict[('  END Reset Field', '   Start timestep')]) + int(
#         cloverDict[('      Start Hydro', '   Start timestep')])
#     cloverDict.pop(('      Start Hydro', '   Start timestep'))
#
#     print(cloverDict)
#     cloverDict.clear()

# Collates data from the same source code section and prints the dictionary. Leaves dict in tact
def calcBenchmark(data, dict, sectionString):
    n = 0
    previousName = "undef"
    for datum in data:
        if n > len(sectionString) - 1:
            currentName = "undef"
        else:
            currentName = sectionString[n]

        if (previousName, currentName) in dict.keys():
            dict[(previousName, currentName)] = int(dict[(previousName, currentName)]) + int(datum)
        else:
            dict[(previousName, currentName)] = datum

        previousName = currentName
        n += 1

    # print(dict)


def insertDict(workloadName, arr, kernelDict):
    s = 0
    if workloadName.__contains__('arm.9.2'):
        arr[0] = list(kernelDict)
        for val in kernelDict:
            s += int(val)
    if workloadName.__contains__('arm.12.2'):
        arr[1] = list(kernelDict)
    if workloadName.__contains__('rv.9.2'):
        arr[2] = list(kernelDict)
    if workloadName.__contains__('rv.12.2'):
        arr[3] = list(kernelDict)
    return s


def extractCP(f):
    global STREAMarm9Total
    global STREAMCombined

    global LBMarm9Total
    global LBMCombined

    global BUDEarm9Total
    global BUDECombined

    global sweeparm9Total
    global sweepCombined

    global cloverarm9Total
    global cloverCombined

    cp = 0
    workloadName = ""
    kernelDict = {}
    for line in f:
        if "Workload:" in line:
            split = line.split(" ")
            try:
                index = split.index("Workload:")
                workloadPathName = split[index + 1]
                lastSlashIndex = workloadPathName.rfind("/")
                if lastSlashIndex != -1:
                    workloadName = workloadPathName[lastSlashIndex + 1:len(workloadPathName)].rstrip()
                    print(workloadName)
                else:
                    print(workloadPathName)

            except ValueError:
                print("Error in printout, no Workload:")
        if "instructions.per.kernel:" in line:
            data = line[len("[SimEng] instructions.per.kernel: "):len(line) - 2].split(",")
            print(data)
            # print(line[len("[SimEng] instructions.per.kernel: "):len(line)-2])

            if workloadName.startswith("LBM"):
                calcBenchmark(data, kernelDict, LBMInstr)
                print(kernelDict)

                kernelDict[('undef', 'Init')] = int(kernelDict[('undef', 'Start')]) + int(
                    kernelDict[('Start', 'Start Timesteps')])
                kernelDict.pop(('undef', 'Start'))
                kernelDict.pop(('Start', 'Start Timesteps'))

                kernelDict[
                    ('File Write', 'undef')] = int(kernelDict[('End Timesteps', 'End')]) + int(
                    kernelDict[('End', 'undef')])
                kernelDict.pop(('End Timesteps', 'End'))
                kernelDict.pop(('End', 'undef'))

                finalArrangment = [kernelDict[('undef', 'Init')], kernelDict[('Start Timesteps', 'End Timesteps')],
                                   kernelDict[('File Write', 'undef')]]

                LBMarm9Total += insertDict(workloadName, LBMCombined, finalArrangment)

                kernelDict.clear()
            elif workloadName.startswith("STREAM"):
                calcBenchmark(data, kernelDict, STREAMInstr)
                print(kernelDict)

                # Combine like sections
                # Setup
                kernelDict[('undef', 'Setup')] = int(kernelDict[('undef', 'Main')]) + int(
                    kernelDict[('Main', 'Start Copy')])
                kernelDict.pop(('undef', 'Main'))
                kernelDict.pop(('Main', 'Start Copy'))

                # Summary
                kernelDict[('Summary', 'undef')] = int(kernelDict[('End MultAdd', 'Start Copy')]) + int(
                    kernelDict[('End MultAdd', 'End')]) + int(kernelDict[('End', 'undef')])
                kernelDict.pop(('End MultAdd', 'Start Copy'))
                kernelDict.pop(('End MultAdd', 'End'))
                kernelDict.pop(('End', 'undef'))

                finalArrangment = [kernelDict[('undef', 'Setup')], kernelDict[('Start Copy', 'Start Scale')],
                                   kernelDict[('Start Scale', 'Start Add')], kernelDict[('Start Add', 'Start MultAdd')],
                                   kernelDict[('Start MultAdd', 'End MultAdd')], kernelDict[('Summary', 'undef')]]

                STREAMarm9Total += insertDict(workloadName, STREAMCombined, finalArrangment)

                kernelDict.clear()
            elif workloadName.startswith("BUDE"):
                calcBenchmark(data, kernelDict, BUDEInstr)
                print(kernelDict)

                kernelDict[
                    ('undef', 'Setup')] = int(kernelDict[('undef', 'START')]) + int(
                    kernelDict[('START', ' Start Fasten')])
                kernelDict.pop(('undef', 'START'))
                kernelDict.pop(('START', ' Start Fasten'))

                kernelDict[
                    ('Validate', 'undef')] = int(kernelDict[(' End Fasten', ' End')]) + int(
                    kernelDict[(' End', 'undef')])
                kernelDict.pop((' End Fasten', ' End'))
                kernelDict.pop((' End', 'undef'))

                finalArrangment = [kernelDict[('undef', 'Setup')], kernelDict[(' Start Fasten', ' End Fasten')],
                                   kernelDict[('Validate', 'undef')]]

                BUDEarm9Total += insertDict(workloadName, BUDECombined, finalArrangment)

                kernelDict.clear()
            elif workloadName.startswith("SWEEP"):
                calcBenchmark(data, kernelDict, sweepInstr)

                # Combine first part of outer loop with inner loop
                kernelDict[('End Energy Groups Loop', 'Loop Over Energy Groups')] = int(
                    kernelDict[('End Energy Groups Loop', 'Loop Over Energy Groups')]) + int(
                    kernelDict[('Loop over Octants', 'Loop Over Energy Groups')])
                kernelDict.pop(('Loop over Octants', 'Loop Over Energy Groups'))

                print(kernelDict)

                kernelDict[
                    ('undef', 'Init')] = int(
                    kernelDict[('undef', 'Start')]) + int(
                    kernelDict[('Start', 'Start Sweep')]) + int(
                    kernelDict[(
                        'Start Sweep', 'Loop over Octants')])

                kernelDict.pop(('undef', 'Start'))
                kernelDict.pop(('Start', 'Start Sweep'))
                kernelDict.pop((
                    'Start Sweep', 'Loop over Octants'))

                kernelDict[
                    ('Finalise', 'undef')] = int(
                    kernelDict[('End Energy Groups Loop', 'End Octant Loop')]) + int(
                    kernelDict[('End Octant Loop', 'End Sweep')]) + int(
                    kernelDict[('End Sweep', 'END')]) + int(
                    kernelDict[('END', 'undef')])

                kernelDict.pop(('End Energy Groups Loop', 'End Octant Loop'))
                kernelDict.pop(('End Octant Loop', 'End Sweep'))
                kernelDict.pop(('End Sweep', 'END'))
                kernelDict.pop(('END', 'undef'))

                finalArrangment = [kernelDict[('undef', 'Init')],
                                   kernelDict[('End Energy Groups Loop', 'Loop Over Energy Groups')],
                                   kernelDict[('Loop Over Energy Groups', 'End Energy Groups Loop')],
                                   kernelDict[('Finalise', 'undef')]]

                sweeparm9Total += insertDict(workloadName, sweepCombined, finalArrangment)

                kernelDict.clear()
            elif workloadName.startswith("CL"):
                calcBenchmark(data, kernelDict, cloverInstr)

                # Add small preloop count to interloop count
                kernelDict[('  END Reset Field', '   Start timestep')] = int(
                    kernelDict[('  END Reset Field', '   Start timestep')]) + int(
                    kernelDict[('      Start Hydro', '   Start timestep')])
                kernelDict.pop(('      Start Hydro', '   Start timestep'))

                print(kernelDict)

                kernelDict[('undef', 'Init')] = int(
                    kernelDict[('undef', 'Start')]) + int(
                    kernelDict[('Start', '      Start Hydro')])
                kernelDict.pop(('undef', 'Start'))
                kernelDict.pop(('Start', '      Start Hydro'))

                kernelDict[('Summary', 'undef')] = int(
                    kernelDict[('  END Reset Field', '        End Hydro')]) + int(
                    kernelDict[('        End Hydro', 'undef')])
                kernelDict.pop(('  END Reset Field', '        End Hydro'))
                kernelDict.pop(('        End Hydro', 'undef'))

                finalArrangment = [
                    kernelDict[('undef', 'Init')],
                    kernelDict[('  END Reset Field', '   Start timestep')],
                    kernelDict[('   Start timestep', '   Start PdV True')],
                    kernelDict[('   Start PdV True', ' Start Accelerate')],
                    kernelDict[(' Start Accelerate', '  Start PdV False')],
                    kernelDict[('  Start PdV False', '  Start Flux Calc')],
                    kernelDict[('  Start Flux Calc', '  Start Advection')],
                    kernelDict[('  Start Advection', 'Start Reset Field')],
                    kernelDict[('Start Reset Field', '  END Reset Field')],
                    kernelDict[('Summary', 'undef')]]

                cloverarm9Total += insertDict(workloadName, cloverCombined, finalArrangment)

                kernelDict.clear()

            workloadName = ""


# /print out raw kernel information
# compile numbers of the same section
#     input: raw kernel info as csv, print output of kernel count output: collated kernel counts as csv
#     Vars: Global dictionary{print pair, count sum}
#     iterate through print output:
#       look at current and previous print, this defines the section for which the corresponding count refers
#       Create dictionary entry if none exist
#       If entry exists, read value, add raw number and update entry
#
# Print dictionary, but need to do some fiddling to get in correct order and sum different sections
# Print raw values and summed values

def normalise(arrOfArr, normFactor):
    for elem in arrOfArr:
        for a in range(len(elem)):
            elem[a] = int(elem[a]) / normFactor


def main():
    # print (str(sys.argv))
    dirString = sys.argv[1]
    directory = os.fsencode(dirString)

    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        f = open(dirString + filename, "r")
        extractCP(f)
        f.close()

    normalise(STREAMCombined, STREAMarm9Total)
    normalise(LBMCombined, LBMarm9Total)
    normalise(BUDECombined, BUDEarm9Total)
    normalise(sweepCombined, sweeparm9Total)
    normalise(cloverCombined, cloverarm9Total)

    print()
    print('Norm Arrays')
    print('STREAM:', end='')
    print(STREAMCombined)
    print('LBM:', end='')
    print(LBMCombined)
    print('BUDE:', end='')
    print(BUDECombined)
    print('sweep:', end='')
    print(sweepCombined)
    print('clover:', end='')
    print(cloverCombined)


# Combine like sections for each benchmark
# Normalise on AArch64 9.2
# Print array

if __name__ == '__main__':
    main()
