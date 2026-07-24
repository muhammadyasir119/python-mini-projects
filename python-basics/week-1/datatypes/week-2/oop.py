# Week 2 - Day 1 (OOP)

# Class banayi
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Object banaya
s1 = Student("Ali", 20)
s2 = Student("Yasir", 22)

s1.show()
s2.show()
