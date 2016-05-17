def countLetters(line):
    """ Count all letter characters in string line.

      The number of letter characters must be returned by the function.
      Examples:
       countLetters('abA1 23') -> returns 3
       countLetters('!') -> returns 0
    """

    #Checks if a character is a letter and counts
    #letters only
    cnt = 0
    for char in line:
        if char.isalpha():
            cnt += 1

    #returns the result
    return cnt
