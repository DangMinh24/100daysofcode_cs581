# day 002 of 100 days of code

"""
Q2: If the statements
x = 3
y = 9
z = "2.4"
have been executed, then evaluate the following expressions. If an error
occurs, state why:
x/y
x//y
x%y
y/x*z
float(x)/float(z)
float(x)//float(z)
int(x)//int(z)
"""

x = 3
y = 9
z = "2.4"


print(x/y)  # result: 0.333, result is a real value
print(x//y)  # result: 0, // operator is integer division.
print(x % y)  # result: 3, % operator is remainder finder.
# print(y/x*z)  # error, can not multiply string type z with float.

# result: 1.25 = 3/2.4 = 30/24, convert string z to float z, then do the division.
print(float(x)/float(z))

# result: 1.0 = 3//2.4 = 30//24, convert string z to float z, then do the integer division.
print(float(x)//float(z))

# error, can not convert '2.4' to integer.
print(int(x)//int(z))
