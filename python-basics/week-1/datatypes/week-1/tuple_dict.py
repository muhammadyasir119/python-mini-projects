# Day 7 - Tuple & Dictionary

# TUPLE
numbers = (1, 2, 3, 4)

print(numbers)
print(numbers[0])


# DICTIONARY
student = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

print(student)

# Access value
print(student["name"])

# Add new key
student["grade"] = "A"
print(student)

# Loop
for key, value in student.items():
    print(key, ":", value)
