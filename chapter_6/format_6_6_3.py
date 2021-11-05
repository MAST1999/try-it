"""
QUICK CHECK: THE FORMAT() METHOD What will be in x when the following
snippets of code are executed?:
"""


def main():
    """This is the start of the application"""

    long_string = "{1:{0}}".format(3, 4)
    # the first number is the width of the field, the second is the number to be formatted in that field
    # 4
    print(long_string)

    long_string = "{0:$>5}".format(3)
    # $>5 means right justified, 5 spaces, and $ means use the currency symbol in the field
    # $$$$3
    print(long_string)

    long_string = "{a:{b}}".format(a=1, b=5)
    # this is rather obvious, but it's a good example of how to use the format method
    # 1
    print(long_string)

    long_string = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
    # this is a combination of the other two snippets
    # 1:$$$$3
    print(long_string)


if __name__ == "__main__":
    main()
