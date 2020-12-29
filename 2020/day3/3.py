from itertools import cycle


with open('data.txt') as fp:
    d = fp.read()


d = d.split('\n')
#print(d)

y = [10]
"""length = range(10, len(d))
for n in length:
    y.append(n) 
#print(y)
"""

count = 0

v = 1
h = 3
h_l = [2, 1, 0]
while v <= 10: 
    print("v is %s, h is %s" % (v, h))
    print(d[v][h])
    if d[v][h] == "#":
        count += 1
        print("eerste 10 count is: %s" % (count))
    v += 1
    h += 3
    print("vbegin is %s" % (v))
while v <= 32:

    for hpos in cycle(h_l):
        h = hpos
        for vpos in y:
            while (h <= 30): 
                print("v is %s, h is %s" % (v, h))
                print(d[v][h])
                if d[v][h] == "#":
                    count += 1
                    print("count is: %s" % (count))
                v += 1
                h += 3

print(count)

