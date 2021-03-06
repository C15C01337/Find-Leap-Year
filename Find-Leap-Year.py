#Devloped By C15C01337 (Bishal Aryal)
#Follow me on Twitter username @C15C01337

print("Devloped By C15C01337 (Bishal Aryal)")
print("Follow me on Twitter username @C15C01337")


year_input = int(input("Enter the year you want to find leap year:"))  #first ask year as a input from user

def is_leap_year(user_year):    #define a function
    
    if user_year % 4 == 0 and user_year % 400 == 0: # use the condition to find a leap year
        print(f"{user_year} is a leap year")
    else:
        print(f"{user_year} is not a leap year")
    
is_leap_year(year_input)  # call the function

