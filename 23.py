def f(ns, nf):
    if ns == nf:
        return 1
    if ns<nf:
        return 0
    return f(ns-8,nf)+f(ns // 2,nf)
print (f(102,43)*f(43,5))
