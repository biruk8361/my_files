import math
print(""" -----------------------------------------------
|                                               |
|                                               |
|    Welcome to python program that used in     |
|              cordinate geometry               |
|                                               |
|                                               |
 ----------------------------------------------- 
 """)
print('''=================================================
= ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ =
=                                               =
=              Operation short key              =
=                                               =
= <Enter "d" for distance between two points>   =
= <Enter "m" for mid-point with out ratio(Two   =
=  equal parts>                                 =
= <Enter "p" for line segment division by point =
=  with ratio>                                  =
=                                               =
= ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ =
=================================================
''')
def dis():
    print('''Distance between two points
    ''')
    print("Please insert only number")
    print()
    x1 = input("Enter x1 : ")
    x2 = input("Enter x2 : ")
    y1 = input("Enter y1 : ")
    y2 = input("Enter y2 : ")
    
    if len(x1) == 0 or len(x2) == 0 or len(y1) == 0 or len(y2) == 0:
        o = input("You didn't fill some values do you want to Start again (y or n)? ")
        if o == y or o == Y:
            start()
    else:
        s1 = (int(x2) - int(x1))**2
        s2 = (int(y2) - int(y1))**2
        s3 = (int(s1) + int(s2))
        s4 = math.sqrt(s3)
        print(str(s4) + " units")
        print()
def mid():
    print('''Mid-point calculation (Two equal parts)
    ''')
    print("Please insert only number")
    print()
    x1 = input("Enter x1 : ")
    x2 = input("Enter x2 : ")
    y1 = input("Enter y1 : ")
    y2 = input("Enter y2 : ")

    if len(x1) == 0 or len(x2) == 0 or len(y1) == 0 or len(y2) == 0:
        o = input("You didn't fill some values do you want to Start again (y or n)? ")
        if o == y or o == Y:
            start()
    else:
        s1 = (int(x1) + int(x2))/2
        s2 = (int(y1) + int(y2))/2
        print("M = ({0}, {1})".format(s1, s2))

def point():
    print(''' line segment division by point with ratio
    ''')
    print("Please insert only number")
    print()
    x1 = input("Enter x1 : ")
    x2 = input("Enter x2 : ")
    y1 = input("Enter y1 : ")
    y2 = input("Enter y2 : ")
    m = input("Enter m : ")
    n = input("Enter n : ")

    if len(str(x1)) == 0 or len(str(x2)) == 0 or len(str(y1)) == 0 or len(str(y2)) == 0 or len(str(m)) == 0 or len(str(n)) == 0:
        o = input("You didn't fill some values do you want to Start again (y or n)? ")
        if o == "y" or o == "Y":
            start()
    else:
        s1 = (int(n)*int(x1) + int(m)*int(x2))/(int(n)+int(m))
        s2 = (int(n)*int(y1) + int(m)*int(y2))/(int(n)+int(m))
        print("R(xo,yo) = ({0}, {1})".format(s1, s2))
def start():
    x = input("Enter short key of operation : ")
    if x == "d" or x == "m" or x == "p":
        if x == "d":
            dis()
        if x == "m":
            mid()
        if x == "p":
            point()
    else:
        print()
        print("Invalid operation please read the manual again")
        print()
        start()
start()

