# task 1. write your name on the screen
print("Piotr")


# variable for number

x = 5

# variable for text (string)

y = "Hello it is me"

# check the type of the variable
print(type(x))

# create a list of numbers

list1 = [4, 5 , 45]

# print(list1[0])

for i in list1:
    print(i)


student1 = {
    "name": "Piotr",
    "age": "41"
}    

print(student1['name'])


if x == 4:
    print('good grade')
else:
    print('other grade')


class Student:
    def __init__(self, name):
        self.name = name

s1 = Student('peter')

print(f"Student: {s1.name}")


class Person:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

p1 = Person('piotr', 41)

print(p1.name)
print("Total number of people is", Person.counter)



