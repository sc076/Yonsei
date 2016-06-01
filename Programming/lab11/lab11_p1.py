def addDialyTemp(mydict, day, temperature):
    """Add key 'day' and value 'temperature' to the dictionary 'mydict'
    only if key 'day' does not already exist in the dictionary.
    The resulting dictionary is returned"""

    if not day in mydict.keys():
        mydict[day] = temperature

    return mydict
