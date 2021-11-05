"""
QUICK CHECK: STRINGS TO NUMBERS
Which of the following will not be converted to numbers, and why?
int('a1')
int('12G', 16)
float("12345678901234567890")
int("12*2") 
"""
# does not convert because a doesn't mean anything in the base of 10
# a = int("a1")
# not convertible
# b = int("12G", 16)
c = float("12345678901234567890")  # this is convertable
d = int("122")  # this is convertable
# not convertable
# e = int("12*2")

# print(a)
# print(b)
print(c)
print(d)
