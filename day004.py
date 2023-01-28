# day 004 of 100 days of code

"""
Q4: What is printed with the following statements?
a) print (int("23"))
b) if 3**2+4**2 == 5**2:
        print ("345")
    elif 3**2 < 4**2:
        print ("34")
    else:
        print ("5")
c) if "toast" < "jam":
        print ("toast")
    else:
        print ("jam")
d) if "12" < "5":
        print ("12")
    else:
        print ("5")
e) a = 12.3
        b = 100
        c = 0
    if a < b: a = a + 1; b = b -1
        c = c – b
        print (a)
        print (c)
f) a = 100
        b = 200
        c = 300
        ab = a<b
        cd = (c == a+b)
    if ab and cd:
        print ("AB and CD")
    elif ab:
        print ("AB")
    else:
        print ("Nope")
"""


print(int("23"))  # result: 23, convert string to integer


# result: 345, since 3**2+4**2 == 25 == 5**2
if 3**2+4**2 == 5**2:
    print("345")
elif 3**2 < 4**2:
    print("34")
else:
    print("5")


# result: jam, since 't' < 'j':
if "toast" < "jam":
    print("toast")
else:
    print("jam")

# result: 12, since '1' < '5':
if "12" < "5":
    print("12")
else:
    print("5")


# result: 13.3 = 12.3 + 1, -99 .
a = 12.3
b = 100
c = 0
if a < b:
    a = a + 1
    b = b - 1
    c = c - b
    print(a)
    print(c)


# result: AB and CD. since ab is true (100 < 200), cd is true (300 == 100 + 200)
a = 100
b = 200
c = 300
ab = a < b
cd = (c == a+b)
if ab and cd:
    print("AB and CD")
elif ab:
    print("AB")
else:
    print("Nope")
