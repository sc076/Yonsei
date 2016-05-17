def findAt(email_addr):
    """ Returns the index of the @ character in an email address.

      findAt('user@cs.yonsei.ac.kr') -> 4
      findAt('@.foo.bar') -> -1 (error, user name empty)
      findAt('foo@.ba@r') -> -1 (error, multiple @ signs not allowed)
      findAt('foo@')      -> -1 (error, domain name empty)
      findAt('foo.bar')   -> -1 (error, no @ sign)
      No other errors need to be checked!
    """

    #Through try exception checks the if the email address is compitable and
    #returns the result
    try:
        address = email_addr.split('@')
        if len(address[0]) == 0 or len(address[1]) == 0:
            return -1
        elif email_addr.count('@') != 1:
            return -1

        return email_addr.find('@')
    except IndexError:
        return -1
