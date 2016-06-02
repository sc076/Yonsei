class Range:
    def __init__(self, start, upper):
        self.__start = start
        self.__end = upper

    def __str__(self):
        output = str(self.__start) + '...' + str(self.__end)
        return output

x = Range(12, 13)
print(x)
