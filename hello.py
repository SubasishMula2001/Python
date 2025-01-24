print("Hello Python")
a = 200 # Integer
Number = 123.12 #float
name = "subasish" #String
is_active = True #boolean
numbers = [10,20,30,40,50,67] #list sequence of order items

a = 5
b = 2
#loop
for i in range(5):
    print("Simple :",i)

count = 0
while count < 5:
    print("Count is: ", count)
    count += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
    
#if ,elif

age = int(input("Enter your age"))
if age >= 18:
    print("You are elligible to vote")
else:
    print("You are not elligible to vote")
    
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# Functions and Scope

def greet(name):
    print(f"Hello , {name} ")
    
greet("Subasish")

def add(a , b):
    return a + b
result = add(3,5)
print(result)

def greet(name="Guest"):
    print(f"Hello, {name}")
greet()
greet("Boo")

# Variable scope 
def example():
    x = 10
    print(x)
    
example()
print(x)

x = 20
def example2():
    print(x)
example2()

x = 10
def change_global():
    global x
    x = 20
change_global()
print(x)
# lambda : anonymous functions, used for short tasks

multiply = lambda a,b : a*b
print(multiply(3,4))

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
# name = input("Enter your name : ")
# print(f"Hello, {name}")
# print("Hello " + name + " ")


# print(type(is_active))
# print(numbers)
# print(is_active)
# print(name)
# print(Number)
# print(a)