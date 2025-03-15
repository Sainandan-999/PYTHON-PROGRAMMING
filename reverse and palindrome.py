n=int(input("enter the number"))
rev=0
p=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
if(p==rev):
    print("it is palindrome")
else:
    print("it is not palindrome")

