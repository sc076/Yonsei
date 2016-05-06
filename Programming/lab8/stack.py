#Stack module
def getStack():
    """Creates and returns an empty Stack"""
    return []

def isEmpty(s):
    """Returns True if stack empty, otherwise returns False. """

    if s == []:
        return True
    else:
        return False

def top(s):
    if isEmpty(s):
        return None
    else:
        return s[len(s)-1]

def push(s, item):
    s.append(item)

def pop(s):
    if isEmpty(s):
        return None
    else:
        item = s[len(s)-1]
        del s[len(s)-1]
        return item
