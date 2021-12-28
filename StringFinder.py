import configparser
import sys
from Helper import SearchFiles
from Helper import OutputData
from Helper import RegexHelp


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

    Strings = RegexHelp.makeRegexExpression(x)

    rootDir = config.get('Test','RootDirToSearch')

    foundMatchesDict = RegexHelp.findStringsInFile(SearchFiles.findValidFiles(rootDir,'txt'), Strings)

    OutputFile = config.get('Test', 'OutputFilename')
    OutputData.saveDataToFile(OutputFile, foundMatchesDict)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
