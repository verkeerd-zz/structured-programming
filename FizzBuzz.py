for i in range(1, 101):        # repeats 100 times with i = 1 to 100
    if i % 5 == 0:
        if i % 3 == 0:         # prints fizzbuss if i can be divided by 3 and 5
            print('fizzbuzz')
        else:                  # prints buzz if i can be divided by 5
            print('buzz')
    elif i % 3 == 0:           # prints fizz if i can be divided by 3
        print('fizz')
    else:                      # prints i if i can be divided by 3 nor 5
        print(i)
