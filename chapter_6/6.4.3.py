"""
QUICK CHECK: STRIP
If the string x equals "(name, date),\n", which of
the following would return a string containing "name, date"?
x.rstrip("),")
x.strip("),\n")
x.strip("\n)(,")
"""

STRING = "(name, date),\n"

# print(string.rstrip("),"))

# print(string.strip("),\n"))

# This would
print(STRING.strip("\n)(,"))
