"""
QUICK CHECK: SPLIT AND JOIN
How could you use split and join to change
all the whitespace in string x to dashes, such as changing "this is a test"
to "this-is-a-test"?
"""

"""
    1. "asdkfj  sdajf sdf asdf   adsofjj"
    2. splitter -> " " and splits using this string and puts in a list
    3. joiner -> gets a list of strings and joins them using the specified string
    4. use the splitter to split the string and store the result in a list
    5. the use the list with the joiner function to create the target string
    6. you have the string with all of the spaces replaced with dash
"""


X = "this is a test"
Y = X.split()
Z = "-".join(Y)
print(Z)
