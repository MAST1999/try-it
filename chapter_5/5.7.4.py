"""
TUPLES: Explain why the following operations aren’t legal for
the tuple x = (1, 2, 3, 4):
x.append(1)
x[1] = "hello"
del x[2]
If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?
"""

x = (2, 1, 4, 3)

# All of these are illegal because they are tring to change the tuple but tuples are
# immutables meaning they can't change
# x.append(1)
# x[1]
# del x[2]

print(x)

x = tuple(sorted(x))

print(x)
