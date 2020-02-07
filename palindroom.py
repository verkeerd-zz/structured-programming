def palindroom_recursive(string):
    """
    takes a sting (string) as input. returns True if the given string is a palindroom. this function uses recurstion.
    """
    string = string.upper()
    if len(string) < 3:
        if string[0] == string[-1]:
            return True
        else:
            return False
    elif string[0] == string[-1]:
        if palindroom_recursive(string[1:-1]):
            return True
    return False


def palindroom_stand_function(string):
    """
    takes a sting (string) as input. returns True if the given string is a palindroom. Uses the function reversed()
    built into the standard library of python.
    """
    string = string.upper()               # converts the string to all uppercase characters.
    negative = "".join(reversed(string))  # copies and reverses the string
    mid = len(string) // 2                # determines the middle index
    if string[:mid] == negative[:mid]:    # returns true if the string and the reversed string match
        return True                       # until the middle index
    return False


def palindroom(string):
    """
    takes a sting (string) as input. returns True if the given string is a palindroom.
    """
    string = string.upper()
    negative = string[::-1]
    mid = len(string) // 2
    if string[:mid] == negative[:mid]:
        return True
    return False
