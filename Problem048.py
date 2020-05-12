from time import time

def loop():
    m=0
    for i in range(1,1001,1): 
        m+=(i**i)
    return m

answer = k[-10:-1]

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(answer))
    print("Time Taken:{}".format(time() - start))
