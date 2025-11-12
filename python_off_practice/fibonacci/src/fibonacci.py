def fibonacci(n: int):
    """
    Print the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        print("Please enter a positive integer.")
        return

    a, b = 0, 1
    sequence = []
    i = 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", sequence)

# Example usage:
terms = int(input("Enter the number of terms: "))
fibonacci(terms)