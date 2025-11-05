
"""
    Prints a spruce tree pattern of a given size.

    The spruce tree consists of a triangle made of asterisks ('*') with increasing width,
    centered using spaces, followed by a single asterisk representing the trunk.

    Parameters:
    size (int): The height of the spruce tree (number of lines in the triangle part).

    Example:
    If size = 3, the output will be:
        a spruce!
          *
         ***
        *****
          *

"""

def spruce(size):
    print("a spruce!")
    i = 1
    line = size
    while line > 0:
        print(" "*(line - 1) + "*"*i)
        line -= 1
        i += 2
    print(" "*(size - 1)+"*")


lenght = int(input("Enter size of the spruce: "))
spruce(lenght)