'''
 Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
i = input("Enter the set values separated by space: ")
v=set(map(int,i.split()))
max_val=max(v)
min_val=min(v)
print(f"max:{max_val}")
print(f"min:{min_val}")
