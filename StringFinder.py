import configparser
import re
import os
import sys
import time

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def findValidFiles(rootDir, fileType):

    paths = []
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.lower().endswith(fileType.lower()):
                paths.append(os.path.join(root, file))

    return (paths)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def detailsOnMatches(detailsOnMatches):
    #remove duplicates that is up to the user to find all of a specific keyword
    return list(set(detailsOnMatches))
    #can add more details if desired to each found entry

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def findStringsInFile(searchFilePaths, strings):

    foundMatches = dict()

    for eachFile in searchFilePaths:
        print("Checking: " + eachFile)
        textfile = open(eachFile, 'r')
        filetext = textfile.read()
        textfile.close()
        matches = re.findall(strings, filetext, re.IGNORECASE)
        if len(matches) > 0:
            foundMatches[eachFile] = detailsOnMatches(matches)

    return foundMatches

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def makeRegexExpression(SearchForList):

    Strings = str('(?:')
    for Each in SearchForList:
        Strings += Each
        #if not last value in list
        if Each is not SearchForList[-1]:
            Strings += '|'

    Strings += ')'

    return Strings

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    #find txt files.
    config = configparser.ConfigParser()
    config.read('Input.txt')

    if not config.has_section('Test'):
        print("missing required fields")
        sys.exit(1)

    # replace remove white spaces
    #split make list
    x = str(config.get('Test','SearchFor').replace(" ", "")).split(",")

    Strings = makeRegexExpression(x)

    rootDir = config.get('Test','RootDirToSearch')

    foundMatchesDict = findStringsInFile(findValidFiles(rootDir,'txt'), Strings)


    #break into a fcn
    OutputFile = config.get('Test','OutputFilename')
    OutputFile = time.strftime("%Y%m%d-%H%M%S--") + OutputFile
    f = open(OutputFile, "a")
    for key, value in foundMatchesDict.items():
        f.write('file:  %s:     Strings Found:  %s\n' % (key, value))
    f.close()


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
