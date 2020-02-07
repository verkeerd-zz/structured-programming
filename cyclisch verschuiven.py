import binascii

def cyclical_moving(character, moving_coefficient):
    """
    takes a character(character) and a number (moving_coefficient) as input. Converts the character to a byte and
    shifts the characters of the byte depending on the moving_coefficient.
    The binary number is shifted to the left if the moving_coefficient is bigger than 0.
    The binary number is shifted to the right if the moving_coefficient is smaller than 0.
    The binary number is shifted for moving_coefficient steps.
    """
    character = ord(character)  # converts the character to its ascii character value.
    binary = '{:b}'.format(character)  # converts the ascii character value to it's binary representation.
    while len(binary) < 8:  # adds 0's to the beginning of the binary number if the binary number doesn't have 8 chars.
        binary = '0' + binary
    if moving_coefficient > 0:               # if the moving coefficient is bigger than 0
        while moving_coefficient != 0:       # repeats n (moving coefficient) times
            binary = binary[1:] + binary[0]  # shifts all 8 characters in the binary number to the left (with carry).
            moving_coefficient -= 1
    if moving_coefficient < 0:                 # if the moving coefficient is smaller than 0
        while moving_coefficient != 0:         # repeats n (moving coefficient) times
            binary = binary[-1] + binary[:-1]  # shifts all 8 characters in the binary number to the right (with carry).
            moving_coefficient += 1
    return binary  # returns the shifted binary number.
