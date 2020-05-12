from math import factorial as fact
from time import time

def digit(n):
    s=[]
    k=n
    while(k>0):
       s.append(k%10) 
       k=k//10
    s.reverse()
    return s

answer = sum(digit(fact(100)))

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(answer))
    print("Time Taken:{}".format(time() - start))
