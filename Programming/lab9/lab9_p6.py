def bubbleSort(alist):
    """ Using the Bubble Sort method sorts the list
        containing tuples.
    """
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][0]>alist[i+1][0]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def search(element_ls, letter):
    """
        Method for searching through the elements of the alphabet counter list
    """

    for subls in element_ls:
        if letter in subls:
            return True
    return False

def countAllLetters(line):
    """ Counts letters in 'line' and returns result list.

      Note 1: the list of letters must be sorted alphabetically.
      Note 2: your letters in the result-list must be stored in lower-case.
    """

    counter = []

    #Makes all the letters lowercase
    line = line.lower()

    #Checks if the letter is already in the list and if it is a letter at all
    for letter in line:
        if letter.isalpha() != False and search(counter, letter) == False :
            counter.append((letter, line.count(letter)))

    #Sorts all of the entries
    bubbleSort(counter)
    return counter
