import os
import sys


def extractCP(f):
    cp = 0
    for line in f:
        if "Workload:" in line:
            split = line.split(" ")
            try:
                index = split.index("Workload:")
                workloadPathName = split[index + 1]
                lastSlashIndex = workloadPathName.rfind("/")
                if lastSlashIndex != -1:
                    print("\n" + workloadPathName[lastSlashIndex + 1:len(workloadPathName)].rstrip(), end=": ")
                else:
                    print(workloadPathName, end=": ")

            except ValueError:
                print("Error in printout, no Workload:")
        if "critical.path.length" in line:
            split = line.split(" ")
            try:
                index = split.index("critical.path.length:")
                cp = int(split[index + 1])
                print("CP = " + str(cp), end="")
            except ValueError:
                print("Error in printout, no critical.path.length:")
        if "instructions:" in line:
            split = line.split(" ")
            try:
                index = split.index("instructions:")
                pathLength = int(split[index + 1])
                ilp = pathLength / cp
                print(" , pathLength = " + str(pathLength) + " , ILP = " + str(ilp), end="")
                cp = 0
            except ValueError:
                print("Error in printout, no instructions:")


def main():
    # print (str(sys.argv))
    dirString = sys.argv[1]
    directory = os.fsencode(dirString)

    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        f = open(dirString + filename, "r")
        extractCP(f)
        f.close()
        print()


if __name__ == '__main__':
    main()
