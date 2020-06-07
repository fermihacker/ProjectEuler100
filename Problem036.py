def dig(n):
    i=0
    k=n
    while(k>0):
        i+=1
        k=k//10
    return i

def pall(n):
    p=0
    m=0
    k=n
    i=dig(n)
    while k>0:
        m=k%10      
        p+=m*(pow(10,i))
        i-=1
        k=k//10
    return p//10

def check(n):
    if pall(n)==n:
        return True

def convert(n):
    b=bin(n)
    k=int(b.replace('0b',""))
    return k

def loop(n):
    i=0
    s=[]
    while(i<=n):
        if(check(convert(i))==True and check(i)==True):
            s.append(i)
        i+=1
    return s

print(sum(loop(pow(10,6))))

#------------------------------------------------------------------------------------------------------------------------------
#Problem's solution redone:

from time import time

pall = lambda n : str(n) == str(n)[ : : -1]

check = lambda n : pall(n) and pall(bin(n).replace('0b',''))

main = lambda : sum([i for i in range(1,10**6) if check(i)])

if __name__ == "__main__":
    start = time()
    print('Answer:{}'.format(main()))
    print("Time taken:{}".format(time() - start))

