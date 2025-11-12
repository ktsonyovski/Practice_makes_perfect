'''
Prime number checker
'''

def is_prime(num: int) -> bool:
    '''
    Fuction which checks if the input integer is prime.
    '''
    if num < 1:
        return False
    
    if num <= 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            i += 6
            return False
        else:
            return True
        

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"The number {number} is prime!")
else:
    print(f"The number {number} is not prime!")