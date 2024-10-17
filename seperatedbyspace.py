...
Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
...
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
...
input_values = input("Enter values separated by space: ")
values_set = set(input_values.split())
print(" ".join(values_set))
...
Enter values separated by space: 2 3 4 5 6 
3 2 6 5 4
