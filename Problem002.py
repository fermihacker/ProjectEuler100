def gen_lis(n):
    s=[]
    a,b,c=1,1,1
    for i in range(1,n+1):
        s.append(c)
        a=b
        b=c
        c=a+b
    return s

def sum_even(n):
    i=0
    s=[]
    while(i<len(fibb)):
        if(fibb[i]>=n):
            break
        if(fibb[i]%2==0):
            s.append(fibb[i])
        i+=1
    return sum(s)

sum_even(4*pow(10,6))
