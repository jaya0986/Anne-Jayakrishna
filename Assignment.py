"""l = [-1,-2,-3,4,5,6]
large = l[0]
for i in l:
    if i > large:
        large = i
print(large)"""
"""l = [-1,-2,-3,4,5,6]
sum = 0
large = l[0]
small = l[0]
for i in l:
    if i > large:
        large = i
    elif i < small:
        small = i
print(large,small)
sum  = large + small
print("Largest number",large)
print("smallest number",small)
print("sum of largest and smallest numbers:",sum)"""
"""str = input("Enter a character:")
for char in str:
    print(char)"""

"""m = input("Enter a string:")
n = input ("Enter a string:")
while m<=n:
    print(m)
    m+=1
else:
    m>=n:
    print(m)
    m-=1"""

"""s = input("Enter a string:")
for i in s:
    if i in 'AEIOUaeiou':
        print(i)"""

"""s = input("Enter a string:")
for i in s:
    if ((i>='A' and i<='Z') or (i>='a' and i<='z')) and (i not in 'AEIOUaeiou'):
        print(i)"""

"""str = input("Enter a string:")
i = len(str)-1
for j in str:
    print(str[i], end = "")
    i-=1"""

"""s = input("Enter a string:")
for i in range(len(s)):
    if i % 2 == 0:
        print(s[i])"""

"""s = input("Enter a string: ")
for i in range(len(s)):
    if i % 2 != 0:
        print(s[i])"""

n = int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range (1,n+1):
        if i+j == n+1 or ((i==2) and (j==2)) or ((i==4) and (j==4)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
print()

    

    



    




        


        
    




        


    
    

    
    
    

 




        
    

   



   



    
    
    

