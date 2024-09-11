days=int(input("Enter the number of days : "))
years=int(days/365)
days-=years*365
weeks=int(days/7)
days-=weeks*7
print("Years: ",years)
print("weeks : ",weeks)
print("days: ",days)