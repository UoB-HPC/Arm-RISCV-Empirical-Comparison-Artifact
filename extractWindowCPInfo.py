import os
import sys
import math

outString = ""


def getILPofWindow(dataList):
    listInput0 = dataList[0].split(",")
    listInput5 = dataList[1].split(",")

    combinedInput = []
    for i in range(len(listInput0) - 1):
        combinedInput.append(int(listInput0[i]) + int(listInput5[i]))

    s = 0
    for i in range(len(combinedInput)):
        s += (i + 1) * combinedInput[i]

    mew = s / sum(combinedInput)

    # Find standard deviation
    # s2 = 0
    # for i in range(len(combinedInput)):
    #     s2 += combinedInput[i] * (((i + 1) - mew) ** 2)
    #
    # delta = math.sqrt(s2 / sum(combinedInput))

    return len(combinedInput) / mew


# Requires run is of only 1 binary, any number of window sizes but only 2 offsets (e.g. 0 and 0.5), offsets for the same
# window size must be run in succession, runs must be in the order of smallest window size to largest
def extractCP(f):
    global outString
    linesUntilData = -1
    dataList = []
    for line in f:
        linesUntilData -= 1

        if "critical.path.per.window:" in line:
            linesUntilData = 3

        if linesUntilData == 0:
            # get data
            dataList.append(line)
            # determine if it is time to collate
            if len(dataList) == 2:
                # Calculate average ILP if all data available
                outString += str(getILPofWindow(dataList)) + ","
                dataList = []


def main():
    global outString
    outString = ""
    dirString = sys.argv[1]
    directory = os.fsencode(dirString)

    first = True
    for file in sorted(os.listdir(directory)):
        if first:
            first = False
        else:
            outString += "\n"
        filename = os.fsdecode(file)
        outString += filename + " "
        f = open(dirString + filename, "r")
        extractCP(f)
        f.close()
        # Remove last comma and close list
        outString = outString[:-1]

    print(outString)


if __name__ == '__main__':
    main()
