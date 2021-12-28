import time

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def saveDataToFile(outputFile, outputDict):

    outputFile = time.strftime("%Y%m%d-%H%M%S--") + outputFile
    f = open(outputFile, "a")
    for key, value in outputDict.items():
        f.write('file:  %s:     Strings Found:  %s\n' % (key, value))
    f.close()