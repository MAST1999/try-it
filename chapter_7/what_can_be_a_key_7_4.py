"""
QUICK CHECK: WHAT CAN BE A KEY?
Decide which of the following expressions can be a dictionary key:
1; 'bob'; ('tom', [1, 2, 3]); ["filename"]; "filename"; ("filename", "extension")
"""


def main():
    """Start of the application"""
    random_dict = {}
    random_dict[1] = "one"
    random_dict["bob"] = "bob"
    # random_dict[("tom", [1, 2, 3])] = "tom"
    # error because the tuple has a list inside which is mutable
    # random_dict[["filename"]] = "filename in brackets" -> error because the list is mutable
    random_dict["filename"] = "filename string"
    random_dict[("filename", "extension")] = "filename extension"

    print(random_dict) # type: ignore


if __name__ == "__main__":
    main()
