'''
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''
i1 = input("Enter the set values separated by space: ")
s1 = set(map(int, i1.split()))
i2 = input("Enter the set values separated by space: ")
s2 = set(map(int, i2.split()))
c=s1.intersection(s2)
sort=sorted(c)
print(' '.join(map(str, sort)) + ' ')
