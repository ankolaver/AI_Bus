import random
finalcoor = open('coor.txt', 'w')

bus1latlon = [(1.297353, 103.858873), (1.296923, 103.859321)]

for k in range(34):
    a = random.uniform(1.28,1.29)
    b = random.uniform(103.81,103.88)
    bus1latlon.append((a,b))

print(bus1latlon)
for item in bus1latlon:
    finalcoor.write(item)
