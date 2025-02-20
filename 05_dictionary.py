def update_age(std_list=None):
    if not std_list:
        return True
    for std in std_list:
        if std.get('name') == 'Jane':
            std['age'] = 50

    return std_list


std_list = [{'name': 'John', 'age': 25},
 {'name': 'Jane', 'age': 24},
 {'name': 'Tom', 'age': 30}]

# std_list = False

updated_std = update_age(std_list)

print(updated_std)



