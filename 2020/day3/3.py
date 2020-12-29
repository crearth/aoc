with open('data.txt') as fp:
    d = fp.read()

#print(d)

d = d.split('\n')

#print(d)

y = []
length = range(0, len(d))
for n in length:
    y.append(n) 
#print(y)

x = 0
d_n = []
while x < len(d):
    mod = x % 2
    if mod <= 0:
        d_n.append(d[x]) 
    x += 1

xc = 4
xx = 1 
while xc < len(d_n):
    for c in d_n:
        print(c[xc])
        print(xc)
        if xc < 31:
            xc += 3 
        else:
            xc = xx
            xx += 1

"""xc = 4
yc = 0
while xc < len(d[0]):
    print(d[yc][xc])
    if xc < 23:
        xc += 3
    else:
        xc = 4
    yc += 1
    """
