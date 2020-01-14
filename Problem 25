def gen_term(a,b):
    return (a+b)

def count(n):
    k=n
    c=0
    while(k>0):
        c+=1
        k=k//10
    return c

def loop_0(n):
    i=0
    a=0
    b=1
    c=1
    s=[0,1,1]
    while(i<n):
       a=b 
       b=c
       c=a+b
       s.append(c)
       i+=1 
    i=0
    while(i<len(s)):
        if(count(s[i])==1000):
            print(i)
            break
        i+=1
