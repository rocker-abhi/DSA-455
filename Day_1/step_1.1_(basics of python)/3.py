"""
    if  else
"""
 # make the driver license program for better understanding of python .
 
age = int(input("please enter your age : "))

if age < 18:
    # here age is less than 18 
    print("not eligible.")
elif age == 18:
    # here age is equal to 18 
    print("eligible for licence next year ")
else:
    print("eligible")