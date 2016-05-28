from collections import deque
import math


def primelist(x):
    primes = [2,3]
    numbers = deque([])
    for i in range(4,x):
        numbers.append(i)
    while len(numbers) != 0:
        s = numbers.popleft()
        for i in primes:
            if i <= math.sqrt(s)//1:
                if s % i != 0:
                    prime = True
                else:
                    prime = False
                    break
        if prime:
            primes.append(s)
            #print(s)
    return primes
