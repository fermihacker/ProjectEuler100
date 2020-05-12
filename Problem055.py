import time

def isLychrel(n):
 	for i in range(50):
 		n += int(str(n)[ : : -1])
 		if str(n) == str(n)[ : : -1]:
 			return False
 	return True

def main():
     start=time.time()
     return str(sum(1 for i in range(10000) if isLychrel(i)))
     print("Time Taken:{}".format(time.time()-start))
 

if __name__=='__main__':
     print(main())
