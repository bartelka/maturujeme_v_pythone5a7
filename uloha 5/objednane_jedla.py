def scitacka():
    fr = open("objednane_jedla.txt", "r", encoding="utf-8")
    pocet = 0
    for riadok in fr:
        pocet += 1
    print("Pocet objednanych jedal:", pocet)

def jedla():
    fr = open("objednane_jedla.txt", "r", encoding="utf-8")
    dic = {"z":0, "c":0, "m":0, "o":0}
    for i in fr.read():
        if i in dic:
            dic[i] = dic.get(i,0) + 1
    return dic

def pocty():
    vypis = ""
    dic = jedla()
    for i in dic:
        vypis += str(i)+":"+str(dic[i]) +"\n"
    print("Pocty jedotlivych jedal:"+"\n"+vypis)

def do20():
    dic = jedla()
    oznacenia = {"c":"cervena", "m":"modra", "z":"zelena", "o":"oranzova"}
    for i in dic:
        if dic[i] < 20:
            print("Menej ako 20 ludi si objednalo jedlo s oznacenim", oznacenia[i], "\n")

def vypis():
    dic = jedla()
    oznacenia = {"c":"cervena", "m":"modra", "z":"zelena", "o":"oranzova"}
    for i in dic:
        print(dic[i], "ludia si objednali jedlo s oznacenim:",oznacenia[i],)

scitacka()
pocty()
do20()
vypis()
