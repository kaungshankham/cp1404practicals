"""
Random
"""

# import random
#
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# 10

# What was the smallest number you could have seen, what was the largest?
# Smallest number is 5 and largest number is 10

# What did you see on line 2?
# 7
# What was the smallest number you could have seen, what was the largest?
# Smallest number is 3 and largest number is 7
# Could line 2 have produced a 4?
# No because the smallest number is 3 with step 2.

# What did you see on line 3?
# 4.872909812939213
# What was the smallest number you could have seen, what was the largest?
# Smallest number is 2.5 and largest number is 5.5.


"""Write code, not a comment, to produce a random number between 1 and 100 inclusive."""

import random

print(random.uniform(1, 100))
