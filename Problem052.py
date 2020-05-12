import time

def digit_check(a,b):
     s1,s2=[],[]
     for i in str(a):
         s1.append(int(i))
     for i in str(b):
         s2.append(int(i))
     s1.sort()
     s2.sort()
     if s1==s2:
         return True
     return False

def check(n):
     if digit_check(n,2*n) and digit_check(n,3*n) and digit_check(n,4*n) and digit_check(n,5*n) and digit_check(n,6*n):
         return True
     return False

def main():
     i=100
     while True:
         if check(i):
             return i
         i+=1
	

if __name__ == '__main__':
     start=time.time()
     print(main())
     print("Time taken:{}".format(time.time()-start))

