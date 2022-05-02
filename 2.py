for a in range (2):
    for b in range (2):
        for c in range (2):
            for d in range(2):
                f = ((a and b) == (not c)) and (not b or d)
                if f == True:
                    print (a,b,c,d,f)
