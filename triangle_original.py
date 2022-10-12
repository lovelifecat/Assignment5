
def classify(a, b, c):

    c1 = max(a, b, c)
    a1 = min(a, b, c)
    if (a1 == a or a1 == b) and (c1 == a or c1 == b):
        b1 = c
    else:
        if (a1 == a or a1 == c) and (c1 == a or c1 == c):
            b1 = b
        else: b1 = a

    if (a1+b1) < c1 or (a1-b1) > c1:
        print("Please enter valid input")
        return 'invalid'
        exit()
    if a1 == b1 and b1 == c1:
        print('Equilateral')
        return 'Equilateral'
    else:
        if a1 == b1 or b1 == c1 or a1 == c1:
            print('isosceles')
            return 'isosceles'
        else:
            return 'scalene'


def ifright(a, b, c):
    c2 = max(a, b, c)
    a2 = min(a, b, c)
    if (a2 == a or a2 == b) and (c2 == a or c2 == b):
        b2 = c
    else:
        if (a2 == a or a2 == c) and (c2 == a or c2 == c):
            b2 = b
        else:
            b2 = a
    if round(((a2**2) + (b2**2)),3) == round((c2**2),3):
        print('This Triangle is a Right triangle')
        return 'Right'
    else:
        print('this triangle is not a Right Triangle')
        return 'Not Right'
