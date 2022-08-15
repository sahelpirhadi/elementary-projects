x=int(input("Enter a number:"))
minute=x//60
second=x%60
hour=minute//60
a_minute=minute%60
day=hour//24
a_hour=hour%24
print(day,"days",a_hour,"hours",a_minute,"minutes",second,"seconds")
    
  
