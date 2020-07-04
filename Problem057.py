
from math import log10
from time import time


def main():
    Ln, n, a, b = 1000, 3, 2, 0
    for i in range(2, Ln+1):
        n, a = n + 2*a, n + a
        if int(log10(n)) > int(log10(a)): b += 1
    return b


if __name__ == "__main__":
    start = time()
    print("Answer:{}".format(main()))
    print("Time Taken : {}".format(time() - start))
      
