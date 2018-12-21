my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])

print("The index of Happy is ",n_list.index("Happy"))

# Output: 5
print(n_list[1][3])

print(n_list[0])

print(n_list[1])

n_list_new = [["Happy", [2,0,1,5]],"Welcome"]

print(n_list_new[0][1])

print(n_list_new[0][1][0])

print(n_list_new[-1])

print(n_list_new[0][-1][-1])

#numbers={1,5,1,52,6}
#count=numbers.count(1)
#print("The value of count is ",count)
