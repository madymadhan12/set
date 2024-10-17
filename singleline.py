...
Write a program to get the set values in a single line separated by space (including duplicate values) and print the number of elements in the given set.
...
def get_set_values_and_count():
    input_values = input("Enter set values separated by space: ")
    values_list = input_values.split()
    values_set = set(values_list)
    print("Number of elements in the set:", len(values_set))
get_set_values_and_count()
...
Enter set values separated by space: 2 3
Number of elements in the set: 2
