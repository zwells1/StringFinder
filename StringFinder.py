import configparser
import re
import sys

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
#def findFile

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def findStringsInFile(filename, strings):

    textfile = open(filename, 'r')
    filetext = textfile.read()
    textfile.close()
    matches = re.findall(strings, filetext, re.IGNORECASE)

    #if matches exist, get the line numbers of each


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

    findStringsInFile('test.txt', Strings)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
