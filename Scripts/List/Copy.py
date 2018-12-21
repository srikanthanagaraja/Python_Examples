old_list = [1, 2, 3]
new_list = old_list

# add element to list
new_list.append('a')

print('New List:', new_list )
print('Old List:', old_list )

# mixed list
list = ['cat', 0, 6.7]

# copying a list
new_list = list.copy()

# Adding element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List: ', list)
print('New List: ', new_list)

# mixed list
list = ['cat', 0, 6.7]

# copying a list using slicing
new_list = list[:]

# Adding element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List: ', list)
print('New List: ', new_list)