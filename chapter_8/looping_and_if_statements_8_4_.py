"""
TRY THIS: LOOPING AND IF STATEMENTS
Suppose that you have a list x = [1, 3, 5, 0, -1, 3, -2],
and you need to remove all negative numbers from
that list. Write the code to do this.
How would you count the total number of negative numbers in a list
y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]?
What code would you use to print very low if the value of x is below -5, low
if it's from -5 up to 0, neutral if it's equal to 0, high if it's greater than 0 up
to 5, and very high if it's greater than 5?
"""
import copy


def main():
    """Start of the application"""
    list_of_numbers = [1, 3, 5, 0, -1, 3, -2]
    copy_of_list = copy.deepcopy(list_of_numbers)
    for number in copy_of_list:
        if number < 0:
            list_of_numbers.remove(number)

    print(list_of_numbers)

    list_of_numbers = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
    total_negative_numbers = 0
    for list_of_numbers in list_of_numbers:
        for number in list_of_numbers:
            if number < 0:
                total_negative_numbers += 1

    print(total_negative_numbers)

    user_input = int(input("Enter a number: "))
    if user_input < -5:
        print("very low")
    elif user_input < 0:
        print("low")
    elif user_input == 0:
        print("neutral")
    elif user_input < 5:
        print("high")
    else:
        print("very high")


if __name__ == "__main__":
    main()
