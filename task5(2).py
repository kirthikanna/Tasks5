#write a python code using lambda function to check
# every element of a list is an integer or string
my_list = [1,3,5,"apple","orange" ]

# Use a lambda function with the filter() function to check if all elements are either integers or strings
results = list(map(lambda x: isinstance(x, (int,str)), my_list))

# Print the result
print(results)