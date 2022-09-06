#If statement
# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")
#for loop
# Program to iterate through a list using indexing

type = ['Art', 'Musical', 'Movie']

# iterate over the list using index
for i in range(len(type)):
    print("I like", type[i])
#while loop
    # Program to add natural numbers up to sum = 1+2+3+...+n

    n = 10

    # initialize sum and counter
    sum = 0
    i = 1

    while i <= n:
        sum = sum + i
        i = i + 1  # update counter

    # print the sum
    print("The sum is", sum)

#break statement
# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

#Continue
# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
