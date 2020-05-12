from math import sqrt

from time import time

start = time()

temp_list = list(i for i in range(1, 28123) if sum(divisors(i)) > i)

notAbundant = list(i for i in range(1, 28123))

for i in range(len(temp_list)):
 	for j in range(i, 28123):
 		if temp_list[i] + temp_list[j] < 28123:
 			notAbundant[temp_list[i] + temp_list[j]] = 0
 		else:
 			break
      
print("Answer:{}".format(sum(notAbundant)))

print("Time Taken:{}".format(time() - start))
