def sum_length_list(lst):
    """
    takes a list with integer elements as input.
    Returns a tuple with three elements.
    - the total sum of all the elements
    - the amount of elements.
    """
    total_sum = 0
    length = len(lst)  # calculates the amount of elements in the list.
    for i in range(length):
        total_sum += lst[i]  # calculates the sum of all elements in the list.
    return total_sum, length


def average_integers(lst):
    """
    takes a list with integer elements as input.
    Returns the average of the integers.
    """
    total_sum, length = sum_length_list(lst)  # finds the sum and length of the list.
    return total_sum / length  # calculates the average by dividing the total sum by the number of elements in the list.


def average_lists_integers(lst):
    """
    takes a list with list elements as input. The elements are lists with integer elements.
    returns the average of all the lists.
    """
    total_sum = 0
    total_elements = 0
    for i in range(len(lst)):  # repeats the code for every element (data type list) in the list (lst).
        list_sum, list_length = sum_length_list(lst[i])  # finds the sum and length of the list.
        total_sum += list_sum
        total_elements += list_length       # adds the amount of elements of the list of integers
    return total_sum / total_elements  # calculates the mean by dividing the total sum by the number of total elements


def average_list(lst):
    """takes a list with list elements as input. The elements are lists with integer elements.
    returns a tuple with two elements.
    - a list with the averages of the individual lists that input (lst) consists of
    - the average of all the lists."""
    averages = []
    total_sum = 0
    total_elements = 0
    for i in range(len(lst)):  # repeats the code for every element (data type list) in the list (lst).
        list_sum, list_length = sum_length_list(lst[i])  # finds the sum and length of this list.
        total_sum += list_sum  # adds the sum of the elements of this list to the total sum of all the lists.
        total_elements += list_length  # adds the amount of elements of the list of integers
        averages.append(list_sum / list_length)  # calculates the average of the current list and adds it to the list with averages.
    return averages, (total_sum / total_elements)  # calculates the mean by dividing the total sum by the number of total elements. returns the list with averages and the total average of all the lists.


lijst_1 = [1,8,5,3,6,8,3,2,4,5]

lijst_2 = [lijst_1, [2,7,8,4,2,4,6,7,3], [5,7,2,4,6,7]]

print(average_list(lijst_2))


# is it better to have less optimised code so you can re-use your functions more or is it better to have more, more optimalised functions