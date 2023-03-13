#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
neg_list = replace_in_list(my_list, -232, 4)
of_range = replace_in_list(my_list, 455, 1)

print(new_list)
print(my_list)
print(neg_list)
print(of_range)