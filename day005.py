# day 005 of 100 days of code

"""
Q5: The United States measures temperature in Fahrenheit degrees, whereas
Canada uses Celsius. A company is developing an app to convert between the
two for people wanting to ski in Banff or Whistler. The formula to convert
from Celsius degrees C to Fahrenheit degrees F is

    F = C*9/5 + 32

Write a program that will be the basis of this app: it will read a temperature
in Celsius, convert it to Fahrenheit, and print the result.
"""


def Celsius2Fahrenheit(C):
    return C*9/5 + 32


print(Celsius2Fahrenheit(2))
