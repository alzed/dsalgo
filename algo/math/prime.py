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


