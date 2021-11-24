"""
TRY THIS: CREATE A DICTIONARY
Write the code to ask the user for three names and three ages.
After the names and ages are entered, ask the user for
one of the names, and print the correct age.
"""


def main():
    """The start of the application"""
    people: dict[str, int] = {}

    for _ in range(3):
        name = input("Enter a name: ")
        age = int(input("Enter an age: "))
        people[name] = age

    name = input("Enter a name and get the age: ")
    print(f"{name} is {people[name]} years old.")


if __name__ == "__main__":
    main()
