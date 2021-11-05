"""
QUICK CHECK: FORMATTING STRINGS WITH % What would be in the variable x
after the following snippets of code have executed?
"""


def main():
    """This is the start of the application"""
    long_string = "%.2f" % 1.1111
    # 1.11
    print(long_string)
    long_string = "%(a).2f" % {"a": 1.1111}
    # 1.11
    print(long_string)
    long_string = "%(a).08f" % {"a": 1.1111}
    # 1.11110000
    print(long_string)


if __name__ == "__main__":
    main()
