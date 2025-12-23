def is_triangle(a, b, c):
    if a <=0 or b <=0 or c <=0:
        return False
    else:
        sides = [a,b,c]
        sides.sort(reverse=True)
        if sides[0] < sides[1] + sides[2]:
            return True
        else:
            return False
