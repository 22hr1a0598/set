'''
Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
i1=input("first set:")
s1 = set(map(int, i1.split()))
i2=input("sec set:")
s2 = set(map(int, i2.split()))
s1.update(s2)
print(' '.join(map(str, sorted(s1))) + ' ')
