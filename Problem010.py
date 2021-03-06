from math import sqrt; from itertools import count, islice
  
def prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prime_sum():
     s=[]
     for i in range(2,2000000):
         if prime(i):
             s.append(i)
     return sum(s)

print(prime_sum())
