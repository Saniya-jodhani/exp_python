# write a progrm to check that a given number is even or odd

num = int(input('Enter a number'))

if num %2 ==0:
    print("even number")
else:
    print("odd number")


# find largest amoung two numbers

n1 = int(input('Enter first number'))
n2 = int(input('Enter second number'))

if n1>n2:
    print(f"{n1} is largest")
else:
    print(f"{n2} is largest")



# check that a given number is prime or not
num = int(input('Enter a number'))
is_prime = 1
if num>1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = 0
            break   

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

# compund interest and take the value from user

p = float(input('enter principal amount'))
r = float(input('enter rate of interest'))
t = float(input('enter time'))
n = float(input('enter number of times interest applied per time period'))  
ci = (p * (1 + r/100)**(t)) - p
print(f"compound interest is {ci}")


