# Day 6 - Lists

# Create list
numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Ahmed", "Yasir"]

print(numbers)
print(names)

# Access items
print(numbers[0])   # first item
print(names[1])     # second name

# Add item
numbers.append(6)
print(numbers)

# Remove item
numbers.remove(3)
print(numbers)

# Loop through list
for num in numbers:
    print("Number:", num)
