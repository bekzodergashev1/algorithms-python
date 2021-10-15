a,b,c=20,7,10
# kata kichikni aniqlash
def addNames(a,b):
    summa = a + b
    return summa

def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
print(getLargest(-5,6,22/5))

