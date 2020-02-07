string_unencoded = input('Geef een tekst: ')
string_encoded = ''

while True:
    try:
        moving_coefficient = int(input('Geef een rotatie: '))
        break
    except ValueError:
        print('Geef een cijfer.')

for char in string_unencoded:             # repeats the code for every character in the string.
    if char != ' ':                       # runs the code if the character isn't a blankspace.
        ascii_value = ord(char)           # computes the ascii value of the character
        ascii_value += moving_coefficient # computes the ascii value with the moving coefficient
        if ascii_value < 65:  # adjusts ascii value if the computed ascii value does not represent an alphabetic char
            ascii_value = 123 - 65 + ascii_value
        elif ascii_value > 91 and ascii_value < 97: # adjusts ascii value
            ascii_value = ascii_value - 91 + 97
        elif ascii_value > 123: # adjusts ascii value
            ascii_value = ascii_value - 123 + 65
        string_encoded += chr(ascii_value)
    else:
        string_encoded += ' '

print('Ceasarcode: ' + string_encoded)
