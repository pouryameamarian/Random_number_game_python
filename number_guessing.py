#   input --> system--> output  
import random
inp1 = random.randint(0, 10) 
inp2 = int(input())
while inp1 != inp2:
    if inp2 > inp1:
        print("it's very big")
        inp2 = int(input())
    elif inp2 < inp1:
        print("it's very small")
        inp2 = int(input())

print("Great!! it's True")
