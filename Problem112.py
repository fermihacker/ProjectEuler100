from time import time

increasing = lambda n : list(str(n)) == sorted(list(str(n))) 

decreasing = lambda n : list(str(n)) == sorted(list(str(n)), reverse = True) 

bouncy = lambda n : not (increasing(n) or decreasing(n))


def proportion(upper_limit):
     k = len([1 for i in range(101, upper_limit) if bouncy(i)])
     return (k/(upper_limit - 100)) *100

def main():
     i = 1500000   # because after testing, the proportion is very close to 99 after this number...
     while True:
         if proportion(i) == 99:
             return "Answer is :{}".format(i)
         i+=1

if __name__ == "__main__":
     start = time()
     print(main())
     print("Time Taken:{}".format(time() - start))
