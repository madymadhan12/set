...
 Write a program to get n number of values in separate line for set and print the values with space separation.
...
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
...
Solution
...
n = int(input("Enter the number of values: "))
values_set = set()
for _ in range(n):
    value = input("Enter a value: ")
    values_set.add(value)  
print(" ".join(values_set))
...
Enter the number of values: 5
Enter a value: 2
Enter a value: 3
Enter a value: 4
Enter a value: 5
Enter a value: 6
3 6 4 5 2
