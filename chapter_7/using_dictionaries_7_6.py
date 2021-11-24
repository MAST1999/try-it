"""
TRY THIS: USING DICTIONARIES
Suppose that you’re writing a program that works like a spreadsheet.
How might you use a dictionary to store the contents of a sheet?
Write some sample code to both store a value and retrieve a
value in a particular cell. What might be some drawbacks to this approach?
"""


def main():
    """Start of the application"""
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("The naming scheme is like this: A1-A10, B1-B10, ...and J1-J10.")

    # Create a dictionary to store the values
    sheet = {}
    for row in rows:
        for column in columns:
            # sheet.setdefault(row + str(column), "")
            sheet[row + str(column)] = ""

    # Store values in the dictionary
    input_number_of_values = int(
        input("How many values would you like to enter? ")
    )
    for _ in range(input_number_of_values):
        input_cell = input("Enter the cell: ")
        input_cell_value = input("Enter the value: ")
        sheet[input_cell] = input_cell_value

    input_cell = input("Enter a cell to get the value: ")
    print(f"The value of the cell is: {sheet[input_cell]}")


if __name__ == "__main__":
    main()
