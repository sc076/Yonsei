def reduceWhitespace(line):
    """ Removes extra whitespace between words and returns the result. """
    front = ''
    back = ''

    #Because the problem is stating to remove blanks only between the words
    #Here we check if there are any blanks in the front and back and copy them
    for char in line:
        if char != ' ':
            break
        front += char

    counter = 0
    revers = line[::-1]

    for idx in range(1, len(revers)):
        if revers[idx] != ' ':
            break
            print(counter)
        counter += 1
        back += revers[idx]

    #Removes the front and back if there is anny
    line = line.lstrip(front).rstrip(back[::-1])

    #Splits the rest by blanks
    line = line.split(' ')
    words = []

    #Remove blanks
    for word in line:
        if word != '':
            words.append(word)

    #Concatanate the words and adds the front and the back
    line = front + ' '.join(words) + back

    #Returns the result
    return line
