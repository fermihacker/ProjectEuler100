from time import time

def digit(n):
    s=[]
    k=n
    while(k>0):
       s.append(k%10) 
       k=k//10
    s.reverse()
    return s

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(sum(digit(2**1000))))
    print("Time Taken:{}".format(time() - start))
