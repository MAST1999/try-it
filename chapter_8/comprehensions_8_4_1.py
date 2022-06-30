"""
TRY THIS: COMPREHENSIONS
What list comprehension would you use to process the list x so that all negative values are removed?
Create a generator that returns only odd numbers from 1 to 100.
(Hint: A number is odd if there is a remainder if divided by 2;
use % 2 to get the remainder of division by 2.)
Write the code to create a dictionary of the numbers and their cubes from 11 through 15.
"""


def main():
    """Start of the application"""
    list_of_numbers = [1, 3, 5, 0, -1, 3, -2]
    list_of_numbers = [number for number in list_of_numbers if number > 0]
    print(list_of_numbers)

    odd_numbers = (num for num in range(100) if num % 2 == 1)
    print(odd_numbers)

    cubes = {num: num ** 3 for num in range(11, 16)}
    print(cubes)


if __name__ == "__main__":
    main()
