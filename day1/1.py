with open('data.txt') as f:
    r_data = f.readlines()

r_data_a = [int(x.split("\n")[0]) for x in r_data]

#print(r_data)
#print(r_data_a)

for x in r_data_a:
    if 2020-x in r_data_a:
        print(x, 2020-x, x*(2020-x))
