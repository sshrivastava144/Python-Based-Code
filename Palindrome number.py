
# write a program to check a aplindrome or not a palindroe
n=int(input("enter the number"))
f=n
rev=0
while n>0:
    rev=(rev*10)+n%10
    n=n//10
if rev==f:
    print(rev,"is a palindrome")
else:
    print(rev,"is not a palindrome number")