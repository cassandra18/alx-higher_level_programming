#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
new_list = copy_list(my_list)
print(new_list == my_list)
print(new_list is my_list)
