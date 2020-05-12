from time import time

isPall = lambda s : s==s[::-1]

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
