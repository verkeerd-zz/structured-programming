def count(list):
    """
    takes a list (list) as input. asks the user for an integer and prints the amount the number appears in the list.
    """
    while True:  # asks the user for an integer. Keeps asking for the right input if the user gives a wrong data type.
        try:
            number = int(input('Geef een geheel getal: '))
            break
        except:
            print('Foute invoer. Geef een geheel (rationeel) getal.')

    total = 0
    for i in range(len(list)):
        if number == list[i]:  # compares the number to each element of the list
            total += 1         # adds one every time the number is found.

    print('Getal ' + str(number) + ' komt ' + str(total) + ' keer voor in de lijst.')


def maximum_difference(list):
    """
    takes a list (list) as input. prints the biggest difference between two consecutive numbers and at which indexes
    these numbers can be found.
    """

    maximum = 0  # currently found biggest difference between two consecutive list elements.
    index = 0  # first index of the two indexes between which the currently biggest difference has been found.
    for i in range(len(list) - 1):
        sum_numbers = abs(list[i] - list[i + 1])  # calculates the difference between two elements by substracting one from the other and taking the absolute value of the result.
        if sum_numbers > maximum:
            maximum = sum_numbers  # replaces the currently found biggest difference
            index = i  # replaces the (first) index at which the biggest difference is found.
    print('Het grootste verschil tussen twee opeenvolgende getallen is ' + str(maximum) +
          '. De twee getallen zijn gelocaliseerd op index ' + str(index) + ' en ' + str(index + 1) + '.')


def gouverning(list):
    """
    takes a binary list(list) as input. checks if the list meets the (2) requirements.
    requirements:
    - there are more 1's than 0's.
    - there are no more than 12 0's
    returns True if the requirements are met. otherwise returns False.
    """
    count_0 = 0
    count_1 = 0
    for number in list:    # iterates for each item of the list.
        if number == 0:    # adds one to the 0 counter for each 0
            count_0 += 1
        else:              # adds one to the 0 counter for each 0
            count_1 += 1
    if count_1 > count_0:  # checks if there are more 0's than 1's.
        if count_0 < 13:   # checks if there are no more than 12 0's.
            return True    # returns true if both the requirements before are met.
    return False           # returns false otherwise
