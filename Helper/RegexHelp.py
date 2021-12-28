import re

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