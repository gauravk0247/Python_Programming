# Q.4 Write a python program to find number is prime or not.
num = int(input("Enter a number: "))
prime = True

for i in range (2, num):
    if (num%i == 0 ):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not prime")