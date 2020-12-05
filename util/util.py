def fileToIntList(fileName):
    with open(fileName) as inputFile:
        return [int(line.strip()) for line in inputFile]

def fileToStringList(fileName):
    with open(fileName) as inputFile:
        return [line.strip() for line in inputFile]

def fileToStringListNoStrip(fileName):
    with open(fileName) as inputFile:
        return [line for line in inputFile]

