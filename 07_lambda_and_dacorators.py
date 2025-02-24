test_lambda = lambda a: a * 10

print(test_lambda(5))

# filter

mylist = [1,2,3,4,5,6,7,8,9,10]

newlist = list(filter(lambda a: a % 2 == 0, mylist))

print(newlist)

# map

newlist = list(map(lambda a: a * 2, mylist))
#
# print(newlist)
#
# # decorators

# decorators with arguments
def my_helper(func):
    def wrapper(*args, **kwargs):
        print('Before calling the function')
        result = func(*args, **kwargs)
        print('After calling the function')
        return result
    return wrapper

@my_helper
def get_total(a, b):
    total = a + b
    print(f"inside get_total function {total}")
    return total

get_total(10, 20)