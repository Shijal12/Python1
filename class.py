class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)



# Output: "This is a person class"
print(Person.__doc__)