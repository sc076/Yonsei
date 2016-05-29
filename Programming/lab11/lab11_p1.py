def addDialyTemp(mydict, day, temperature):
    """Add key 'day' and value 'temperature' to the dictionary 'mydict'
    only if key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned"""

    if not day in mydict.keys():
        mydict[day] = temperature

    return mydict


temp = {'Mon': '20', 'Tue': '30', 'Wed': '12', 'Fri': '23', 'Sat': 25 }

temp_updated = addDialyTemp(temp, 'Sat', '30')
print('Test:', temp_updated)
