class Range:
    def __init__(self, start, upper):
        if start <= upper:
            self.__start = start
            self.__end = upper
        else:
            raise IndexError

    def __str__(self):
        output = str(self.__start) + '...' + str(self.__end)
        return output

    def __lt__(self, range2):
        for r2 in range(range2.__start, range2.__end+1):
            for r1 in range(self.__start, self.__end+1 ):
                if r1 >= r2:
                    return False
        return True
