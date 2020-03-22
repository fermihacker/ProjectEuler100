import num2words

import time

def main():
     start=time.time()
     word = lambda k : num2words.num2words(k).replace(' ','').replace('-','')
     p=''
     for i in range(1,1001):
         p+=word(i)
     print("number of letters used:{}".format(len(p)))
     print("Time Taken:{}".format(time.time()-start))

if __name__=="__main__":
     main()
