def beeramid(bonus, price):
    levels = 0
    if bonus==0 or bonus<0 or price>bonus:
        return 0
    for i in range(1,100):
        bonus-= price * (i*i)
        if bonus>=0:
            levels+=1
        else:
            break    
    return levels
