# day 001 of 100 days of code

"""
Q1: Evaluate the following expressions
a) 3*3/2
b) 3*3//2
c) 3*3%2
d) (3*3)%2
e) 3**3/3
f) (3+2)-(2-4)
g) (3+2)/(2-4)
"""

print(3*3/2)  # result: 4.5, result is returned as real number
print(3*3//2)  # result: 4, operator // is used as integer division.
print(3*3 % 2)  # result: 1, operator % remainder finder.


# result: 1, operator * and operator % have the same priority. Then left -> right order
print((3*3) % 2)

# result: 9 = 3^2, operator ** is power operator.
print(3**3/3)

# result: 7 = 3+2+4-2
print((3+2)-(2-4))

# result: -2.5 = 5/-2, result is real value
print((3+2)/(2-4))
