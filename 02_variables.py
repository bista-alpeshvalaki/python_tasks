a = 10
print("address of A", id(a))

b = 20.50
print("address of B", id(b))

c = 10
print("address of C", id(c))

d = "Hello"

print("address of D", id(d))

std = {"name": "Ravi", "age": 25}

std.update({'address': 'Kathmandu', 'phone': 9867665654})
std['mobile'] = 9867665654

print(" std", id(std))

phone = std.get('xyz', False)
print("phone", phone)

# phone = std['xyz']

is_active = False

# byte string
name = b"Hello"

print("name", name, type(name))

# format string
name = "Hello %s "%std['name']

name = f"Hello {std['name']}"

sum = f"Sum of {a} and {b} is {a+b}"

print("sum", sum)
