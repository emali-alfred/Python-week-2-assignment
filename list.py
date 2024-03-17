# Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by space: ").split()
numbers = [int(num) for num in numbers]

# Compute the sum of integers in the list
sum_of_numbers = sum(numbers)
print("Sum of all the integers:", sum_of_numbers)
