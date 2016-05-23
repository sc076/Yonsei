def getFile():
    """ Returns the file name and associated file object for reading
        the file as a tuple of the form (file_name, input_file)
    """

    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name: ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except IOError:
            print('Input file not found - please reenter\n')

    return (file_name, input_file)

def countWords(file_name, input_file):
    """ Returns the number of the occurances of search_word
        provided input_file object
    """

    # init
    space = ' '
    num_occurances = 0
    word_delimiters = (space, ',', ';', ':', '.', '\n',
                        '"', "'", '(', ')')
    search_word_len = len(search_word)

    for line in input_file:
        end_of_line = False

        # convert line to all lower case chars
        line = line.lower()

        #scan line until end of line reached
        while not end_of_line:
            try:
                # search for word in current line
                index = line.index(search_word)

                # if word at start of line followed by a delimiter
                if index == 0 and line[search_word_len] in word_delimiters:
                    found_search_word = True

                #if search word within line, check chars before/after
                elif line[index - 1] in word_delimiters and \
                    line[index + search_word_len] in word_delimiters:
                        found_search_word = True

                # if found within other letters, then not search word
                else:
                    found_search_word = False

                # if search word found, increment count
                if found_search_word:
                    num_occurrences = num_occurrences+1

                # reset line to rest of line following search word
                line = line[index + search_word_len: len(line)]

            except ValueError:
                end_of_line = True

    return num_occurances

# === main

#program welcome
print('This program will display the number of occurrences of a')
print('specified word within a given text file\n')

# open file to search
file_name, input_file = getFile()

# get search word
search_word = input('Enter word to search: ')
search_word = search_word.lower()

# count all occurrences of search word
num_occurances = countWords(input_file, search_word)

# display results
if num_occurances == 0:
    print('No occurrences of word', "'" + search_word + "'", 'found in file', file_name)
else:
    print('The word', "'" + search_word + "'", 'occurs', num_occurances, 'times in file', file_name)
