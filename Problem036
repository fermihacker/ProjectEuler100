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

sum(loop(pow(10,6)))
