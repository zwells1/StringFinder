import ConfigParser
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
    matches = re.findall("(<(\d{4,5})>)?", filetext)

    #other examples
    s = "These are roses and lilies and orchids, but not marigolds or .."
    r = re.compile(r'\broses\b | \bmarigolds\b | \borchids\b', flags=re.I | re.X)
    print r.findall(s)
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):

    #find txt files.


    #find if specific strings in file exist.
    Strings = ['abc', 'xyz']
    findStringsInFile('test.txt', Strings)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])

