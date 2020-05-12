from time import time

def ret_dig(n, i):
     return int(str(n)[-i:])

if __name__ == "__main__":
     start = time()
     print(main())
     print("Time Taken:{}".format(time() - start))
