def check(a,b,c):
    if a<b<c and (pow(a,2)+pow(b,2)==pow(c,2)):
        return True
    else:
        return False

def loop3(n):
    i=1
    a=3
    b=4
    c=5
    while(i<=n):
        while(a<=n):
            while(b<=n):
                while(c<=n):
                    if check(a,b,c)==True and a+b+c==1000:
                        return a*b*c
                        break
                    else:
                        pass
                    c+=1
                b+=1
                c=3
            a+=1
            b=2
            c=3
        i+=1
        a=1
        b=2
        c=3    

loop3(500)
