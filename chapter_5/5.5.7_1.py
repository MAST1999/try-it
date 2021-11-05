"""
LIST OPERATIONS: What would be the result of len([[1,2]] * 3)?
What are two differences between using the in operator and a list’s index()
method?
Which of the following will raise an exception?: min(["a", "b”, "c"]);
max([1, 2, "three"]); [1, 2, 3].count("one")
"""

print(len([[1, 2]] * 3))

sample = [1, 2, 3, 4, 5]

# in returns boolean, index returns the index of the
# item if it exists otherwise raises an exception
# so it is better to use the together to make sure the item exists and then find the
# index using the index :D
print(1 in sample, sample.index(1))
# print(10 in sample, sample.index(10))

print(min(["a", "b", "c"]))
print([1, 2, 3].count("one"))

# Throws an error
# print(max([1, 2, "three"]))
