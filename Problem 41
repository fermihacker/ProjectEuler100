from math import sqrt; from itertools import count, islice
import itertools as itr
import time
  
def prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
 
def pandigit(n):
     try:
         for i in range(1,n+1):
             if str(n).count(str(i))>1:
                 return False
     except TypeError:
         return False
     except ValueError:
         return False
     return True

def form(s):
     k=''
     for i in s:k+=i
     return k

def gen():
    start=time.time()
    s=list(itr.permutations('1234567',7))
    k=[]
    for i in s:
        k.append(int(form(i)))
    k.sort()
    g=[]
    for i in k:
        if prime(i):
            g.append(i)
    print("Time taken:{}".format(time.time()-start))
    return max(g)

if __name__=='__main__':
	print(gen())
