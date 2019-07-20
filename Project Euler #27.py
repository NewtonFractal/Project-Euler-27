import time
import math
start = time.time()

primelist= [2]

def primefinder(number):
    prime = [True] * (number+1)
    for y in range(3,int(math.sqrt(number+1)),2):
        if prime[y] == True:
            primelist.append(y)
            for x in range(y*y, number + 1,y+y):
                prime[x] = False
    for x in range(y+2,number+1,2):
        if prime[x] == True:
            primelist.append(x)

primefinder(70000)

def Quadratic_primes(record,current):
    for x in range(1,100):
        for a in range(-999,999,2):
            for b in primelist:
                if x**2+a*x+b not in primelist2:
                    break
                if current > record:
                    record = current




Quadratic_primes(0,0)

end = time.time()
print(end - start)
