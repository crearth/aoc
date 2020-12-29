with open('data.txt') as f:
    d = f.read()

d_list = d.replace('\n', ',')[:-1]

d_list = d_list.split(',')

#print(d_list)

count = 0
checks = 0

for i in d_list:
    mini = int(i.split('-')[0])
    maxi = int(i.split('-')[1].split(' ')[0])
    minmax = [mini] 
    while mini < maxi:
        mini = mini + 1
        minmax.append(mini)
    letter = i.split(' ')[1][:-1]
    passw = i.split(' ')[2]

    print("// letter: %s, passw: %s, correct aantal: %s" % (letter, passw, minmax))
    checks += 1

    result = 0
    for char in passw:
        if char == letter:
            result += 1
    print("aantal overeenkomsten: %s" % (result))
    for n in minmax:
        #print("Nu aan het checken: %s" % (n))
        if n == result: 
            count = count + 1
            print("---- OK, passw is: %s" % (passw))

print("checks: %s, count at the end is: %s" % (checks, count))

    #print("min is " + min + ", max is " + max + ", letter is " + letter + ", wachtwoord is " + passw)
