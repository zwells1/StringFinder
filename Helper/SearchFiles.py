import os

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def findValidFiles(rootDir, fileType):

    paths = []
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file.lower().endswith(fileType.lower()):
                paths.append(os.path.join(root, file))

    return (paths)