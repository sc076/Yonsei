def copyFiles(f1, f2, f3):
    """ Copies f1 and f2 onto f3.

      If f1 or f2 cannot be opened, -1 is returned.
      Otherwise, 0 is returned.
    """

    #Tries two open the two files for reading
    #if it is a fail returns -1
    try:
        file1 = open(f1, 'r')
        file2 = open(f2, 'r')
    except:
        return -1

    #Opens/creates the third file ready for writing
    file3 = open(f3, 'w')

    #Reads and writes first the content of the first file
    #Then the second one
    content = file1.read()
    file3.write(content)

    content = file2.read()
    file3.write(content)

    #Closes all of the files after the work is done
    file3.close()
    file1.close()
    file2.close()

    return 0
