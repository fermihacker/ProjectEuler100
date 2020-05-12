import time

from functools import reduce
 
 def factors(n):    
     return set(reduce(list.__add__, 
                 ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
     T = lambda x : x * (x + 1) // 2 
     i=1
     while True:
         if len(factors(T(i)))>500:
             return i,T(i)
         i+=1    

if __name__=="__main__":
     s=time.time()
     print(main())
     print("Time taken:{}".format(time.time()-s))
