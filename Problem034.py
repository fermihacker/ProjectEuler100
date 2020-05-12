def digits(n):
    s=[]
    k=n
    while(k>0):
        s.append(k%10)
        k//=10
    return s

def fact(n):
    m=1
    i=1
    while(i<=n):
        m*=i
        i+=1
    return m

def sum_dig_fact(n):
    s=0
    for i in digits(n):
        s+=fact(i)
    return s

def check(n):
    if sum_dig_fact(n)==n:
        return True

def loop(n):
    i,s=10,[]
    while(i<=n):
        if check(i)==True:
            s.append(i)
        i+=1
    return sum(s)

answer = loop(pow(10,5))

from time import time
if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(answer))
    print("Time Taken:{}".format(time() - start))
