def index_intersection():
    """
    asks the user for two strings. returns the index on which the two given strings deviate.
    """

    string_1 = input('Geef een string: ')
    string_2 = input('Geef nog een string:')
    found = False
    if not found:
        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                found = True
                print('Het eerste verschil zit op index ' + str(i))
                break
        if string_1 == len(string_2):
            print('De strings zijn identiek.')
        elif string_1 > string_2:
            print('Het eerste verschil zit op index ' + str(len(string_2) + 1))
        else:
            print('Het eerste verschil zit op index ' + str(len(string_1) + 1))

index_intersection()