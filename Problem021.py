from functools import reduce
from time import time

def d(n):
    return sum(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) - {n})
                
def main():
    check = lambda a, b : d(a) == b and d(b) == a and a != b
    res = []
    for i in range(1,10000):
        for j in range(1,i + 1):
            if check(i, j):
                res.append(i)
                res.append(j)
                print(i,j)
    return list(dict.fromkeys(res))

if __name__ == "__main__":
  start = time()
  print("Answer : {}".format(sum(main())))
  print("Time Taken : {}".format(time() - start))
