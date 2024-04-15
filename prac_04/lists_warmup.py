"""
3
2
1
3, 1, 4, 1, 5, 9
1,5
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


"""
numbers = [3, 1, 4, 1, 5, 9, 2]

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Print all the elements from numbers except the first two
print(numbers[2:])

# Print whether 9 is an element of numbers
print(9 in numbers)