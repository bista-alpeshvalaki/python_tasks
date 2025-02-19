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

while True:
    print("called after 5 sec.")
    time.sleep(5)
    now = datetime.now() #
    if now.hour == 5:
        break

current = [1,2,3,4,5]
new = []
for i in a:
    if i % 2 != 0:
        continue
    new.append(i)

print(new)
