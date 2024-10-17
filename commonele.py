...
Write a program to print the values which are similar in both given sets.
....
def print_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    if common_elements:
        print("Common elements:", common_elements)
    else:
        print("No common elements found.")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 60, 70}
print_common_elements(set1, set2)
...
Common elements: {40, 30}
