k=0
for b1 in 'авдпр':
    for b2 in 'авдпр':
        for b3 in 'авдпр':
            for b4 in 'авдпр':
                s = b1+b2+b3+b4
                k+=1
                if s.count('п') == 1:
                    if s.count('р') == 1:
                        if s.count('в') == 1:
                            if s.count('д') == 1:
                                print (k)