'''
 Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.

'''
i1=input("enter first set:")
s1=set(map(int,i1.split()))
i2=input("enter sec set:")
s2=set(map(int,i2.split()))
diff=s1.difference(s2)
sort=sorted(diff)
print(' '.join(map(str,sort))+' ')
