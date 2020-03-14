def digits(n):
    k=n
    m=int()
    s=[]
    while(k>0):
        m=k%10
        s.append(m)
        k=k//10
    s.sort()
    return s

def gen_lis(n):   
    i=1
    s=[]
    while(i<=n):
        s.append(i)
        i+=1
    return s

def check_pan(n):
    s=gen_lis(len(digits(n)))
    p=digits(n)
    if(s==p):
        return True

def loop(n):
    x=1
    y=1
    m=''
    b=1
    q=[]
    while(x<=n):
        while(y<=n):
            m=str(y)+str(x)+str(x*y)
            b=int(m)
            if(check_pan(b)==True and len(digits(b))==9):
                q.append(x*y)
            y+=1
        x+=1
        y=0
    q = list(dict.fromkeys(q))
    return q

loop(1000)


	

