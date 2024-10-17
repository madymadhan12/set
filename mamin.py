...
 Write a program to find the maximum and minimum value of given set values python
...
def find_max_min(values):
    if values:
        max_value = max(values)
        min_value = min(values)
        print("Maximum value:", max_value)
        print("Minimum value:", min_value)
    else:
        print("The set is empty.")
values = {10, 20, 30, 40, 50}
find_max_min(values)
...
Maximum value: 50
Minimum value: 10
