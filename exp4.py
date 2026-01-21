#  a program to demonstarte list and tuple in python

my_list = [10,20,30,40]
my_tuple = (10,20,30,40)
print("List element : ")

for i in my_list:
    print(i)

print("Tuple Elements:")
for i in my_tuple:
    print(i)


# a program using a for loop to loop over a sequence

sequence = [1,2,3,4,5]
for i in sequence:
    print(i)

# a program using a while loop that prints a countdown to zero

num = int(input("Enter a number: "))
while num >=0:
    print(num)
    num-=1