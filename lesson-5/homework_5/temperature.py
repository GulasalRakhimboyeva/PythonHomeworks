# ### Task 1

# Write a script called temperature.py that defines two functions:

# 1. _convert_cel_to_far()_ which takes one float parameter representing
#  degrees Celsius and returns a float representing the same temperature
#  in degrees Fahrenheit using the following formula:
#    _F = C \* 9/5 + 32_
# 2. _convert_far_to_cel()_ which take one float parameter representing 
# degrees Fahrenheit and returns a float representing the same temperature
#  in degrees Celsius using the following formula:
#    _C = (F - 32) \* 5/9_

# The script should first prompt the user to enter a temperature 
# in degrees Fahrenheit and then display the temperature converted 
# to Celsius. Then prompt the user to enter a temperature in degrees
#  Celsius and display the temperature converted to Fahrenheit. All 
# converted temperatures should be rounded to 2 decimal places.

# Here’s a sample run of the program:


# Enter a temperature in degrees F: 72
# 72 degrees F = 22.22 degrees C

# Enter a temperature in degrees C: 37
# 37 degrees C = 98.60 degrees F

def convert_cel_to_far(c):
    return round(c*9/5 + 32, 2)


def convert_far_to_cel(f):
    return round((f-32)*5/9, 2)
    

f_input=input('Enter a temperature in degrees Fahrenheit: ')
f=float(f_input)
f_c=convert_far_to_cel(f)
print(f_input, "degrees  F =", f_c, "degrees C")
print()
c_input=input('Enter a temperature in degrees  Celsius: ')
c=float(c_input)
c_f=convert_cel_to_far(c)
print(c_input, "degrees  C=", c_f, "degrees  F")