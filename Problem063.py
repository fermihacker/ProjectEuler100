from time import time

def digits(n):
    s=[]
    k=n
    while(k>0):
        s.append(k%10)
        k//=10
    return len(s)

def loop(n):
    a = 0
    b = 0
    s=[]
    while (a <= n):
        while (b <= n):
            if(digits(a**b)==b):
                s.append(a**b)
            else:
                pass
            b+=1
        b=1
        a+=1
    return s

answer = len(loop(100))

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(answer))
    print("Time Taken:{}".format(time() - start))
