def game(k,h):
    if (h==3) and (k == 1):
        return True
    if (h==3) and (k<1):
        return False
    if (h==3) and (k>1):
        return False
    if (h<3) and (k >1):
        return False
    if (h<3) and (k <1):
        return False
    h +=1
    if h ==1 or h ==3:
        if k % 2 == 0: return game(k - (0.5 * k), h)
        if k % 2 != 0: return game(k - 2, h)
        if k % 3 == 0: return game(k - ((2 / 3) * k), h)
        if k % 3 != 0: return game(k - 3, h)
    if h ==2:
        if k % 2 == 0: return game(k - (0.5 * k), h)
        if k % 2 != 0: return game(k - 2, h)
        if k % 3 == 0: return game(k - ((2 / 3) * k), h)
        if k % 3 != 0: return game(k - 3, h)
for x in range (1,37):
    if game(x,0):
        print (x)
