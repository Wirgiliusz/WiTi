

def loadData(path):
    plik = open(path, "r")
    linie = plik.readlines()
    n = int(linie[0].split()[0])

    zadania = []
    for i in range(1, n+1):
        linia = linie[i].split()
        zadania.append([int(linia[0]),int(linia[1]),int(linia[2]), i])
    plik.close()

    return zadania


zadania = loadData("data/data20.txt")