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

def sieve(integer):
    """ Seive of eratosthenes 
        return all prime numbers upto 'integer' 
    """
    
    is_prime = [1]*(integer+1)
    is_prime[0] = is_prime[1] = 0
    i = 2
    while i*i <= integer:
        if is_prime[i]:
            for j in range(i*i, integer+1, i):
                is_prime[j] = 0
        i += 1
    
    prime = [i for i,v in enumerate(is_prime) if v]

    return prime

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

