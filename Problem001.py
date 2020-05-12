from time import time

main = lambda : sum([i for i in range(1001) if (i % 3 == 0 or i % 5 == 0)])

if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(main()))
    print("Time Taken:{}".format(time() - start))
