def moderatetDays(mydict):
    """Returns a list [...] of the days for which the average
    temperature was between 70 and 79 degrees. """

    avg_temp = []

    #Looks through all pairs key-> value to find a day responding
    #to the condition
    for key in mydict:
        if mydict[key] >= 70 and mydict[key] <= 79:
            avg_temp.append(key)

    #returns the resultng list if no days are found returns an empty list
    return avg_temp

temp = {'Mon': 60, 'Tue': 60, 'Wed': 20, 'Thu': 45, 'Fri': 60, 'Sat': 60, 'Sun': 42}
print(moderatetDays(temp))
