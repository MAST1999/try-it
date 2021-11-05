"""
QUICK CHECK: MODIFYING STRINGS 
What would be a quick way to change all
punctuation in a string to spaces?
"""

import string

sample_string = "I am tired! I ?! like fruit...and milk"
# map punctuation to space
translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
print(sample_string.translate(translator))
