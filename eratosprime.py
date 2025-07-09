def sieve(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return [i for i in range(n+1) if prime[i]]

print(sieve(50))  # In ra các số nguyên tố <= 50
