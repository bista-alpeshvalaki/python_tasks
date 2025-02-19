import time
from datetime import datetime

mylist = [1,2,3,4,5]
mylist2 = []
for i in mylist:
    if i % 2 == 0:
        mylist2.append(i * 5)
print("mylist2", mylist2)


mylist3 = [i * 5 for i in mylist ]

print("mylist3",mylist3)

# while loop

# while True:
#     print("called after 5 sec.")
#     time.sleep(5)
#     now = datetime.now() #
#     if now.hour == 5:
#         break

current = [1,2,3,4,5]
new = []
for i in current:
    if i % 2 != 0:
        continue
    new.append(i)

print(new)

# dictionary
mydict = {'a':1, 'b':2, 'c':3, 'name':'python'}
for key , value in mydict.items():
    name = f"key {key} and value: {value}"
    print(name)


# tuple
my_tuple = (1,2,3)
print("my_tuple", my_tuple, type(my_tuple))

my_tuple = 1,
print("my_tuple", my_tuple, type(my_tuple))


lst1 = [2,3,4]
lst2 = [6,7,8]

for i, j in zip(lst1, lst2):
    print(i*5, j*10)

count = 0
for i in lst1:
    print(count, i)
    count += 1

# enumarate

for index, i in enumerate(lst1):
    print(index, i)

# range
# range(1000)
# range(1, 10)
# range(1, 1000, 10)

# list build in fn

lst5 = [10,20,30,40]
lst5.append(60)

print(lst5)

lst5.insert(0, 100)

print("lst5===========",lst5)

# dict build in fn
student = {'name':'Smith', 'age':20, 'city':'NY' , 'marks': 90}

print(student.keys())

student.pop('city')

print(student.keys())