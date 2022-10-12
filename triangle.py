"""
This is a program to identify the type of triangle and whether it is a right triangle
"""


def classify(a_0, b_0, c_0):
    """It's a function to identify the type of triangle"""

    c_1 = max(a_0, b_0, c_0)
    a_1 = min(a_0, b_0, c_0)
    if (a_1 in {a_0, b_0}) and (c_1 in {a_0, b_0}):
        b_1 = c_0
    else:
        if (a_1 in {a_0, c_0}) and (c_1 in {a_0, c_0}):
            b_1 = b_0
        else: b_1 = a_0

    if (a_1+b_1) < c_1 or (a_1-b_1) > c_1:
        print("Please enter valid input")
        return 'invalid'

    if a_1 == b_1 and b_1 == c_1:
        print('Equilateral')
        return 'Equilateral'

    if a_1 == b_1 or b_1 == c_1 or a_1 == c_1:
        print('isosceles')
        return 'isosceles'

    return 'scalene'


def ifright(a_0, b_0, c_0):
    """It's a function to identify whether the triangle is a right triangle"""
    c_2 = max(a_0, b_0, c_0)
    a_2 = min(a_0, b_0, c_0)
    if (a_2 in {a_0, b_0}) and (c_2 in {a_0, b_0}):
        b_2 = c_0
    else:
        if (a_2 in {a_0, c_0}) and (c_2 in {a_0, c_0}):
            b_2 = b_0
        else:
            b_2 = a_0
    if round(((a_2**2) + (b_2**2)),3) == round((c_2**2),3):
        print('This Triangle is a Right triangle')
        return 'Right'

    print('this triangle is not a Right Triangle')
    return 'Not Right'
