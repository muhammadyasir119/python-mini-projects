# Day 5 - Functions

# Simple function
def greet():
    print("Hello Bhai ")

greet()


# Function with parameter
def greet_user(name):
    print("Hello", name)

greet_user("Yasir")


# Function with return
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)


# Even / Odd using function
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even(10))
