...
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
...
from collections import Counter
def process_input_and_find_duplicates():
    input_values = input("Enter set values separated by space: ")
    values_list = input_values.split()
    value_counts = Counter(values_list)
    duplicates_count = sum(1 for count in value_counts.values() if count > 1)
    unique_values_set = set(values_list)
    print(f"Number of duplicate values: {duplicates_count}")
    print(f"Set of unique values: {unique_values_set}")
process_input_and_find_duplicates()
...
Enter set values separated by space: 2 3  4 5 7
Number of duplicate values: 0
Set of unique values: {'7', '3', '2', '5', '4'}

=== Code Execution Successful ===
