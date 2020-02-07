def fibonaci(n):
    """takes the index of the fibonaci number (n) as input. returns the fibonaci number."""

    if n == 1:
        return 1
    elif n < 1:
        return 0
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)

print(fibonaci(9))