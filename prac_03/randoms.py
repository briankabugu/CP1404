import random


print(random.randint(5, 20))  # line 1
# Smallest number seen is 5 and largest is 20

print(random.randrange(3, 10, 2))  # line 2
# Smallest number seen is 3 and largest is 9
# No, line 2 could not have produced a 4 because the step size is 2 hence only odd numbers are generated.

print(random.uniform(2.5, 5.5))  # line 3
# Smallest number seen is 2.5 and largest is 5.5


print(random.randint(1, 100))

