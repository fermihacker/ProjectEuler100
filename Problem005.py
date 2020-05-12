from time import time

def check(n,a,b):
    for j in range(a,b+1):
        if(n%j!=0):
            return False
            
def main(a,b):
    i=2520
    while True:
        if check(i,a,b)!=False:
            return i
            break
        i+=1

if __name__=='__main__':
    start = time()
    print("Answer:{}".fromat(main()))
    print("Time Taken:{}".format(time() - start))
