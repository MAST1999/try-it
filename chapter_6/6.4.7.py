"""
STRING OPERATIONS: Suppose that you have a list of strings in which
some (but not necessarily all) of the strings begin and end with the double
quote character:
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
What code would you use on each element to remove just the double quotes?
What code could you use to find the position of the last p in Mississippi?
When you’ve found that position, what code would you use to remove just
that letter?
"""

x = ['"abc"', "def", '"ghi"', '"klm"', "nop"]
y: list[str] = []

for some_string in x:
    if some_string[0] == '"':
        y.append(some_string.replace('"', ""))
    else:
        y.append(some_string)

print(y)


miss_string = "Mississippi"
last_p = miss_string.rfind("p")
print(last_p)


new_miss_string = f"{miss_string[:last_p]}{miss_string[last_p + 1:]}"
print(new_miss_string)
