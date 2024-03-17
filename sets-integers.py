# Accept user input to create two sets of integers
set1 = set(input("Enter integers for the first set separated by space: ").split())
set2 = set(input("Enter integers for the second set separated by space: ").split())

# Create a new set containing common elements from both sets
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)
