from time import time

def check(n):
    for i in range(n-1,1,-1):
        if n%i==0:
            return False


def nth_prime(n):
    s,i=[],2
    while(len(s)<n):
        if check(i)!=False:
            s.append(i)
        i+=1
    return s[-1]

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(nth_prime(10001)))
    print("Time Taken:{}".format(time()-start))
