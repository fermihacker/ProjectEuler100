from itertools import islice,count
from math import floor,sqrt
from time import time
from collections import deque

def prime(n):
    if n == 0 or n == 1:
        return None
    if n == 2:
        return True
    return all([not(n % i == 0) for i in islice(count(2),floor(sqrt(n)))])

def checkCircular(n):
    A = deque(list(str(n)))
    if not prime(n):
        return False
    SomeLis = []
    for i in range(len(A)):
        SomeLis.append(int(''.join(list(A))))
        A.rotate()
    return all(prime(i) for i in SomeLis)

def main():
    counter = 0
    k = []
    for i in range(2,10**6):
        if checkCircular(i):
            counter += 1
    return counter

if __name__ == "__main__":
    start = time()
    print("Ans = {}".format(main()))
    print("Time Taken:{}".format(time() - start))
 
    
