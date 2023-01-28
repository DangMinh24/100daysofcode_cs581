# day 003 of 100 days of code

"""
Q3: Given the variable definitions presented, evaluate the following expressions
as being True or False.
x = 12
y = 14

a) x>3
b) x >=12
c) x<y
d) x<y and y>14
e) x<y or y>14
f) not (x == y)j34
g) not(x<y) and not(y>14)
"""

x = 12
y = 14

print(x > 3)  # result: true, 12 is larger than 3
print(x >= 12)  # result: true, 12 is less than 14
print(x < y)  # result: true, 12 is less than 14
print(x < y and y > 14)  # result: false, since (true && false == false)
print(x < y or y > 14)  # result: true, since (true || false == true)
print(not (x == y))  # result: true, since (12 != 14)

# result: false, since ((not true)  and (not false) ) == false
print(not (x < y) and not (y > 14))
