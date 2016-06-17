import os

result = []

def searchDir(directory, s):
    """ Recursively searches 'directory' for .txt files
        that contain string s. """
    files = os.listdir(directory)
    for file in files:
        fullname = directory + '/' + file
        try:
            if os.path.isdir(fullname):
                searchDir(fullname,s)
            else:
                if s in file:
                    result.append(fullname)
        except OSError:
            print('Access denied to: ' + fullname)

    return result
