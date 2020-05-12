from time import time

def main():
    powers = []
    for a in range(2, 101):
        for b in range(2, 101):
            powers.append(a ** b)
    powers = set(powers)
    print(len(powers))
    
    
if __name__ == '__main__':
    start = time()
    print("Answer:{}".format(main()))
    print("Time Taken:{}".format(time() - start))
