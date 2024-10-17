...
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
...
def delete_element_from_set(values, element):
    if element in values:
        values.remove(element)
        print(f"Element {element} has been removed.")
    else:
        print("Given value is not present in the set list.")
values = {10, 20, 30, 40, 50}
element = 30
delete_element_from_set(values, element)
delete_element_from_set(values, 60)
...
Element 30 has been removed.
Given value is not present in the set list.
