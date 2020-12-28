with open('data.txt') as f:
    d = f.read()

d_list = d.replace('\n', ',')[:-1]

d_list = d_list.split(',')

count = 0
checks = 0

def index_check(pos1, pos2, letter, passw):
    return (passw[pos1] == letter or passw[pos2] == letter) and (passw[pos1] != passw[pos2])

for i in d_list:
    pos1 = int(i.split('-')[0])
    pos2 = int(i.split('-')[1].split(' ')[0])
    letter = i.split(' ')[1][:-1]
    passw = i.split(' ')[2]

    print("// letter: %s, passw: %s, slechts een van volgende posities: %s, %s " % (letter, passw, pos1, pos2))

    checks += 1
    
    if index_check(pos1 - 1, pos2 - 1, letter, passw): count += 1

print("checks: %s, count at the end is: %s" % (checks, count))
