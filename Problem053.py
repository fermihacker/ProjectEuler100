from math import factorial
import time

def C(n,r):
     return factorial(n)//(factorial(n-r)*factorial(r))

def main(n):
     s=time.time()
     nums = list(i for i in range(1, n + 1))
     k = 0
     for a in range(0,n):
         for r in range(0,a+1):
             if C(a,r)>pow(10,6):
                 k+=1
             else:
                 pass
     print("Number of values for given upper limit:{}".format(k))
     print("Time taken:{}".format(time.time()-s))

if __name__=="__main__":
      main(101)
