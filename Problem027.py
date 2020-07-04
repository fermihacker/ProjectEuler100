from itertools import islice,count
from math import floor,sqrt
from time import time

def prime(n):
    if n == 0 or n == 1:
        return None
    if n == 2:
        return True
    return all([not(n % i == 0) for i in islice(count(2),floor(sqrt(n)))])

def checkQuad(a,b):
    i = 0
    counter = 0
    while True:
        exprn = pow(i,2) + a*i + b
        if prime(exprn):
            counter += 1
            i += 1
        else:
            return (counter,"n**2 + {}n + {}".format(a,b))
    
    
def main():
    maindict = {}
    for a in range(-1000,1001):
        for b in range(-1000,1000):
            try:
                maindict[checkQuad(a,b)[0]] = checkQuad(a,b)[1]
                if maindict[checkQuad(a,b)[0]] > 1:
                    print(max(maindict))
            except:
                pass
    return maindict[max(maindict)] 

if __name__ == "__main__":
  start = time()
  print("The quadratic expression is:{}".format(main()))
  print("Time Taken:{}".format(time() - start))
