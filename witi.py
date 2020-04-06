import copy

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

def calculate_Fmax(zad):
    S = []
    C = []
    T = []
    F = 0

    S.append(0)
    C.append(zad[0][0])
    T.append(max(C[0]-zad[0][2],0))
    F = zad[0][1] * T[0]
    for j in range(1, len(zad)):
        S.append(C[j-1])
        C.append(S[j] + zad[j][0])
        T.append(max(C[j]-zad[j][2],0))
        F += zad[j][1] * T[j]

    return F
    
def sortD(zad):
    while True:
        zmiana = False
        for j in range(0, len(zad)-1):
            if zad[j][2] > zad[j+1][2]:
                zad[j], zad[j+1] = zad[j+1], zad[j]
                zmiana = True

        if zmiana == False:
            return zad



zadania = loadData("data/data13.txt")
print(calculate_Fmax(copy.deepcopy(zadania)))
zadaniaSortD = sortD(copy.deepcopy(zadania))
print(calculate_Fmax(copy.deepcopy(zadaniaSortD)))