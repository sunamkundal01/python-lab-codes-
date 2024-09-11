#Write a program to find factorial of a number using Iteration.
a= int(input("Enter the number"))
ans=1
for i in range (1,a+1):
    ans*=i
print("factorial is ",ans)    