# Day 4 - Loops

# FOR LOOP
for i in range(1, 6):
    print("Number:", i)


# WHILE LOOP
i = 1
while i <= 5:
    print("While:", i)
    i += 1


# Table print (important)
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
