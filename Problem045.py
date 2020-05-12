from time import time

def main():
     T = lambda n: n * (n + 1) // 2
     P = lambda n: n * (3 * n - 1) // 2
     H = lambda n: n * (2 * n - 1)
     t = set(T(i) for i in range(100000))
     p = set(P(i) for i in range(100000))
     h = set(H(i) for i in range(100000))
     k=t.intersection(p)
     return list(k.intersection(h))[3]


if __name__=="__main__":
     s=time()
     print("Answer:{}".format(main()))
     print("Time taken:{}".format(time()-s))
     
     
