from time import time

isPall = lambda s : str(s)==str(s)[::-1]

def main():
    res = []
    for i in range(100,1000):
        for j in range(100,1000):
            if isPall(str(i*j)):
                res.append(i*j)
    return max(res)
               
if __name__ == "__main__":
    start = time()
    print("Answer:{}".format(main()))
    print("Time taken:{}".format(time()-start))
    
#------------------------------------------------------------------------------------------------------------------------
# A Better solution:

from time import time

isPall = lambda s : str(s)==str(s)[::-1]

main = lambda : max([i*j for (i,j) in enumerate(list(range(100,1001)),100) if isPall(i*j)])

if __name__ == "__main__":
    start = time()
    print("Answer:{}".format(main()))
    print("Time taken:{}".format(time()-start))
