from time import time


def cut(a, b):
     a1 = list(str(a))
     b1 = list(str(b))
     for i in a1:
         if i in b1:
             a1.pop(a1.index(i))
             b1.pop(b1.index(i))
     return int(form(a1)),int((form(b1)))

def form(s):
     k=''
     for i in s:
         k+=i
     return k



def check(a,b):
     if a%10==0 and b%10==0 or a==b:
         return False
     if cut(a,b)[0]/cut(a,b)[1] == a/b:
         return True
     return False



def main():
     s=[]
     for a in range(11,100):
         for b in range(11,100):
             try:
                 if check(a,b):
                     s.append(cut(a,b))
             except ZeroDivisionError:
                 pass
     return s[:4]



if __name__=="__main__":
     s=time()
     print(main())
     print("Time taken:{}".format(time()-s))
