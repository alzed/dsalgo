from random import randint
from gcd import gcd  

def is_prime(integer):
    if integer <= 3:
        return True
    i = 2
    while i*i <= integer:
        if integer%i == 0:
            return False
        i += 1
    return True

def fermat(integer):
    def power(x, y, n):
        if y == 0:
            return 1
        elif y%2 == 0:
            return power((x*x)%n, y//2, n)
        else:
            return (x * power((x*x)%n, (n-1)//2, n))%n

    for _ in range(3):
        a = randint(2, integer-2)
        if not gcd(integer, a) == 1:
            return False
        elif not power(a, integer-1, integer) == 1:
            return False
    return True
    