from math import factorial 
from time import time


digit_fact_sum = lambda n : sum( factorial( int( i ) ) for i in str(n) )


def check_chain(n):
     temp_list,temp_var = [n], n
     count = 0
     if n == digit_fact_sum(n):
         return 1
     while True:
         temp_var = digit_fact_sum(temp_var)
         temp_list.append(temp_var)
         count += 1
         if list(dict.fromkeys(temp_list)) != temp_list:
             return count 


def main():
     counter = 0
     for i in range(1, 10 ** 6 + 1):
         if check_chain(i) == 60:
             counter += 1
     return counter


if __name__ == "__main__":
     start = time()
     print(main())
     print("Time Taken:{}".format(time() - start))

