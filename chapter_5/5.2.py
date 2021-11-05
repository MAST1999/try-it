"""
LIST SLICES AND INDEXES Using what you know about the len()
function and list slices, how would you combine the two to get the second half
of a list when you don’t know what size it is? Experiment in the Python shell
to confirm that your solution works.
"""
import random

x = int(input("enter from: "))
y = int(input("until: "))

random_number = random.randint(x, y)

# sample: list[int] = [num for num in range(random_number)]
sample: list[int] = random.sample(range(1, 1000), random_number)

print(sample[len(sample) // 2 :])
