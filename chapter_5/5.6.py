"""
LIST COPIES: Suppose that you have the following list: x = [[1, 2,
3], [4, 5, 6], [7, 8, 9]] What code could you use to get a copy y of
that list in which you could change the elements without the side effect of
changing the contents of x?
"""

import copy

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

y = copy.deepcopy(x)

y[2][1] = 0

print(x, y)
