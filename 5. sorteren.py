def sort_long_bubble(lst):
    """
    takes a list as input. sorts the list from the lowest numbers to the highest.
    """
    length = len(lst) - 1
    counter = 0  # counts the number of sorted elements.
    while counter < length:  # loops until all items are sorted
        counter = 0  # resets the counter when the algorithm starts at the beginning of the list.
        for i in range(length):
            if lst[i] > lst[i + 1]:  # compares two consecutive indexes
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # switches the two items if the later is bigger than the former
                break  # restarts the sorting algorithm at the beginning of the list after a change has been made.
            counter += 1


def sort_bubble_alt(lst):
    """
    Takes a list as input. sorts the list from the lowest numbers to the highest.
    """
    length = len(lst) - 1
    for i in range(length):          # loops the program for the maximum number of loops needed (loops needed for O)
        for j in range(length):      # checks every two elements on consecutive indexes
            if lst[j] > lst[j + 1]:  # if they are in the right order.
                lst[j], lst[j + 1] = lst[j + 1], lst[j]   # switches two elements if former is bigger than the latter.


def sort_bubble(lst):
    """
    takes a list as input. sorts the list from the lowest numbers to the highest.
    """
    length = len(lst) - 1
    counter = 0  # counts the number of sorted elements.
    while counter < length:  # loops until all items are sorted
        counter = 0  # resets the counter when the algorithm starts at the beginning of the list.
        for i in range(length):
            if lst[i] > lst[i + 1]:  # compares two consecutive indexes
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # switches the two items if the later is bigger than the former
            else:
                counter += 1


lijst = [6,3,8,0,3,6,8,6,4,2,6,8,4,3]

sort_bubble_alt(lijst)

print(lijst)
