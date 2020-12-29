with open('data.txt') as fp:
    d = fp.read()

#print(d)

d = d.split('\n')
d.pop(0) # delete first row
#print(d)

y = []
length = range(0, len(d))
for n in length:
    y.append(n) 
#print(y)

# make array with only odd rows <-- niet nodig
"""x = 0
d_o = []
while x < len(d):
    mod = x % 2
    if mod <= 0:
        d_o.append(d[x]) 
    x += 1
"""

xc = 3 # start on x coordinate 4
xx = 3 # second start (every ten times) 
for r in d:
    if xc <= 31:
        print(xc)
        print(r[xc])
        xc += 3
    elif xc > 31:
        xx -= 1
        xc = xx
        print(r[xc])
        print("xc is %s en xx is %s" % (xc, xx))

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
