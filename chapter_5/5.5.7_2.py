"""
LIST OPERATIONS: If you have a list x, write the code to safely remove
an item if—and only if—that value is in the list.
Modify that code to remove the element only if the item occurs in the list
more than once.
"""

x = [1, 2, 1, 4, 5, 1, 2]

# if it is in the array
# if 1 in x:
#     del x[x.index(1)]

# print(x)

# if there is more than one in the array
def there_is_more_than_one(array: list[int], item: int) -> int:
    number = 0
    if item in array:
        number += 1
        number += there_is_more_than_one(
            array=array[array.index(item) + 1 :], item=item
        )
    else:
        return number

    return number


number_of_items_in_array = there_is_more_than_one(x, 1)

if number_of_items_in_array > 1:
    while number_of_items_in_array > 0:
        del x[x.index(1)]
        number_of_items_in_array -= 1

    print(x)

# use this to make it work easier x.count(item)
