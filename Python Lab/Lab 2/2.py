#Python Program to count the number of vowels in a given string
str =input("enter the String in lower case ")
c=0
for i in range(0,len(str)):
    if(str[i]=='a' or str[i]=='e'or str[i]=='i'or str[i]=='o'or str[i]=='u'):
        c=c+1
print("no. od character in String is :",c)    