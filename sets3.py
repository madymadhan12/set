...
Write a program to print only the different values between two given sets.
...
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
set1 = set(input("Enter elements for the first set separated by space: ").split())
set2 = set(input("Enter elements for the second set separated by space: ").split())
diff = set1.symmetric_difference(set2)
print("Different values between the two sets are:", " ".join(diff))
...
Enter elements for the first set separated by space: 1 2 3 4 
Enter elements for the second set separated by space: 2 5 6 8
Different values between the two sets are: 3 5 6 8 1
