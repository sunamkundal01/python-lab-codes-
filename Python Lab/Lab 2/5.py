#Write a program to find factorial of a number using Recursion.

a= int(input("Enter the number"))
def fact(x):
    if(x==1 or x==0):
        return 1
    else:
        return x*fact(x-1)
        
ans=fact(a)    
print("factorial is ",ans)           