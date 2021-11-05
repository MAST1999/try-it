"""
QUICK CHECK: STRING SEARCHING
If you wanted to check whether a line ends
with the string "rejected", what string method would you use? Would there
be any other ways to get the same result?
"""

string = "This request is rejected"
print(string.endswith("rejected"))

string_len = len("rejected")
print(string[-string_len:] == "rejected")
