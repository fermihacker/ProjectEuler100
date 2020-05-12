from time import time

def sq_sum_lis(n):
    s=[]
    for i in range(1,n+1,1):
        s.append(pow(i,2))
    return s

def sum_sq(n):
    return pow(n*(n+1)/2,2)

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(sum_sq(100)-sum(sq_sum_lis(100))))
    print("Time Taken:{}".fromat(time() - start))
