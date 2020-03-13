def collatz(n):
    s=[]
    while n > 1:
        s.append(n)
        if (n % 2):
            n = 3 * n + 1
        else:
            n = n // 2
    s.append(1)
    return s

def check():
     s=[]
     for i in range(2,pow(10,6)):
         s.append(len(collatz(i)))
     return max(s),s.index(max(s))+2        

check()  #The second number in the tuple is the answer...

