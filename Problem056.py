from time import time

def loop(n):
    s=[]
    p=[]
    a=1
    b=1
    while(a<n):
        while(b<n):
            s.append(digit_sum(a**b))
            p.append(a**b)
            b+=1
        a+=1
        b=1
    v=s.index(max(s))
    return max(s),p[v]

answer = loop(100)

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(answer))
    print("Time Taken:{}".format(time() - start))
