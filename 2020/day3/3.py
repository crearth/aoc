from itertools import cycle



with open('data.txt') as fp:
    d = fp.read()

#print(d)

d = d.split('\n')
#d.pop(0) # delete first row
#print(d)

y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
"""length = range(10, len(d))
for n in length:
    y.append(n) 
    """
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
"""for r in d:
    if xc <= 31:
        print(xc)
        #print(r[xc])
        xc += 3
    elif xc > 31:
        xx -= 1
        xc = xx
        print("xc is %s en xx is %s" % (xc, xx))
        """

v = 1
v_new = 10
h = 3
h_l = [2, 1, 0]
while v <= 10: 
    print(v)
    print(d[v][h])
    v += 1
    h += 3
for hpos in cycle(h_l):
    h = hpos
    for vpos in y:
        while (h <= 30): 
            print("v is %s, h is %s" % (v, h))
            print(d[v][h])
            v += 1
            h += 3

"""
while v <= 322:
    while v <= 10: # van 1 tot en met 10
        print("v is %s, h is %s" % (v, h))
        print(d[v][h])
        v += 1
        h += 3 
    h = 2
    while v <= 20: # van 11 tot en met 20
        print("v is %s, h is %s" % (v, h))
        print(d[v][h])
        v += 1
        h += 3
    h = 1
    while v <= 30: # van 21 tot en met 30
        print("v is %s, h is %s" % (v,h)) 
        print(d[v][h])
        v += 1
        h += 3
    h = 0
    while v <= 40: # van 31 tot en met 40
        print("v is %s, h is %s" % (v, h))
        print(d[v][h])
        v += 1
        h += 3
    h = 2 
    while v <= 50: 
        print("v is %s, h is %s" % (v, h))
        print(d[v][h])
        v += 1
        h += 3
    h = 1
    while v <= 60: 
        print("v is %s, h is %s" % (v,h)) 
        print(d[v][h])
        v += 1
        h += 3
    h = 0
    while v <= 70: 
        print("v is %s, h is %s" % (v, h))
        print(d[v][h])
        v += 1
        h += 3
 
    for position in cycle(reversed(range(len(d[0])))):
        print("v is %s, h is %s" % (v, position)) 
        print(d[v][position])
        v += 1
        """

"""z = 1
x = 3
while z <= 322:
    while x <= 31:
        print(z)
        print(d[z][x])
        x += 3
        z += 1
    x = 2
    while x <= 31:
        print(z)
        print(d[z][x])
        x += 3
        z += 1
        """


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
