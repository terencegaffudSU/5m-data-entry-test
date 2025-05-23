def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if type(x) == int and type(y) == int:
        x = x + y
        y = x - y
        x = x - y
        return ("The new x is " + str(x) + " and the new y is " + str(y))
    else:
        return 0


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
