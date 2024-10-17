...
Write a program to update the given set in another set.
...
def update_set(set1, set2):
    set1.update(set2)
    print("Updated set1:", set1)
set1 = {10, 20, 30}
set2 = {30, 40, 50}
update_set(set1, set2)
...
Updated set1: {50, 20, 40, 10, 30}
