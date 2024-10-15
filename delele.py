'''
Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.

'''
input_values = input("Enter the set values separated by space: ")
values_set = set(map(int, input_values.split()))
element_to_delete = int(input("Enter the element to delete: "))
if element_to_delete in values_set:
    values_set.remove(element_to_delete)
    print(' '.join(map(str, sorted(values_set))) + ' ')
else:
    print("Given value is not present in the set list.")
 
