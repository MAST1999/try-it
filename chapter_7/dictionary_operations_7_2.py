"""
QUICK CHECK: DICTIONARY OPERATIONS
Assume that you have a dictionary x = {'a':1, 'b':2, 'c':3, 'd':4}
and a dictionary y = {'a':6, 'e':5, 'f':6}.
What would be the contents of x after the following snippets of code have executed?:

del x['d']
z = x.setdefault('g', 7)
x.update(y)
"""


def main():
    """This is the start of the application"""
    first_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    second_dict = {"a": 6, "e": 5, "f": 6}

    del first_dict["d"]
    print(first_dict)

    third_dict = first_dict.setdefault("g", 7)
    print(third_dict)

    first_dict.update(second_dict)
    print(first_dict)


if __name__ == "__main__":
    main()
