
age = input("Enter your age: ")
try:
    age = int(age)
except ValueError:
    print("Please enter a valid age")

#if else
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

name = input("Enter your name: ")

# if elif else
if (age >= 18 and age < 100) or name == 'admin':
    print("You are eligible to vote")
elif age == 17 or age == 16:
    print("You will be eligible to vote next year")
elif age == 16:
    print("You will be eligible to vote in two years")
else:
    print("You are not eligible to vote")


# match case

print("match case")
