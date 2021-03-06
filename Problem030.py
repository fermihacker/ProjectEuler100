def digit(n):
    k,s=n,[]
    while(k>0):
        s.append(k%10)
        k//=10
    return s

def check(n):
    k=[]
    for i in digit(n):
        k.append(i**5)
    if(sum(k)==n):
        return True


def loop(n):
    s,i=[],2
    while i<=n:
        if(check(i)==True):
            s.append(i)
        i+=1
    return sum(s)

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(loop()))
    print("Time Taken:{}".format(time() - start))
   
