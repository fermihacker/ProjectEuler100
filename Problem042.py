from time import time

T = lambda n : n * (n + 1) // 2

tNums = [T(i) for i in range(1000)]

nameNum = lambda s : sum([ord(i) - 64 for i in s])

check = lambda s : nameNum(s) in tNums

def getWords():
    tempStr = ''    
    with open('p042_words.txt', 'r') as f:
        for i in f.readlines():
            tempStr += i
        out = tempStr.split(',')
    k = []
    for i in out:
        k.append(i[1:len(i) - 1])
    return sorted(k)

main = lambda : sum([1 for i in getWords() if check(i)])

if __name__ == "__main__":
    start = time()
    print('Answer:{}'.format(main()))
    print("Time taken:{}".format(time() - start))

