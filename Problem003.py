def is_Prime(n):
    k=n-1
    while(k>2):
        if(n%k==0):
            return False
        k-=1

def factor(n):
    for k in range(n-1,1,-1):
        if n%k==0 and is_Prime(k)!=False:
            return k
            break
            
