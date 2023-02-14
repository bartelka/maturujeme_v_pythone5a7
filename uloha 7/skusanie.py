import random
ps = 30
po = 50

if po < ps:
    print("Pocet otazok je mensi ako pocet studentov.")

def vytvor_zoz(pocet):
    zoz = []
    for i in range(1,pocet+1):
        zoz.append(i)
    return zoz

studenti = vytvor_zoz(ps)
otazky = vytvor_zoz(po)

random.shuffle(studenti)

def random_priradenie(zoz1:"studenti",zoz2:"otazky"):
    dic = {}
    x = (zoz2[0])%2
    for i in zoz1:
        z = random.choice(zoz2)
        while x == z%2:
            z = random.choice(zoz2)
        x = z%2
        dic[i]=dic.get(i,z)
        zoz2.remove(dic[i])
        print("student:", i, "cislo otazky:", dic[i])

random_priradenie(studenti, otazky)
