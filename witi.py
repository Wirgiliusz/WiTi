import copy
import math
from itertools import permutations

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
    Fmax = 0

    S.append(0)
    C.append(zad[0][0])
    T.append(max(C[0]-zad[0][2],0))
    Fmax = zad[0][1] * T[0]
    for j in range(1, len(zad)):
        S.append(C[j-1])
        C.append(S[j] + zad[j][0])
        T.append(max(C[j]-zad[j][2],0))
        Fmax += zad[j][1] * T[j]

    return Fmax
    
def sortD(zad):
    while True:
        zmiana = False
        for j in range(0, len(zad)-1):
            if zad[j][2] > zad[j+1][2]:
                zad[j], zad[j+1] = zad[j+1], zad[j]
                zmiana = True

        if zmiana == False:
            return zad

def optPermutations(zad):
    perms = list(permutations(zad,r=len(zad)))
    Fmax = math.inf
    for perm in perms:
        F = calculate_Fmax(perm)
        if F < Fmax:
            Fmax = F
    return Fmax

def optRecursionStart(zad):
    availableTasks = copy.deepcopy(zad)
    currentTasks = []
    Fmax = math.inf
    n = len(zad)

    def optRecursion(zad, current):
        nonlocal Fmax
        nonlocal n
        availableTasks = copy.deepcopy(zad)
        currentTasks = copy.deepcopy(current)

        if len(zad) != 0 and currentTasks != n:
            for i in range(0, len(availableTasks)):
                currentTasks.append(copy.copy(availableTasks[i]))
                temp = availableTasks.pop(i)
                optRecursion(availableTasks, currentTasks)
                availableTasks.insert(i, temp)
                currentTasks.pop()
        else:
            #print(currentTasks)
            F = calculate_Fmax(copy.deepcopy(currentTasks))
            if F < Fmax:
                Fmax = F

    optRecursion(availableTasks, currentTasks)
    return Fmax

def dynamicIterations(zad):
    availableTasks = copy.deepcopy(zad)
    currentTasks = []
    knownValues = {}
    Fmin = math.inf

    for i in range(1, 2**len(zad)):
        binTasksToCheck = bin(i).replace("0b","")
        if binTasksToCheck not in knownValues:
            iterator = 0
            for binChar in reversed(binTasksToCheck):
                if binChar == '1':
                    currentTasks.append(availableTasks[iterator])
                iterator = iterator + 1

            sumOfP = pSum(copy.deepcopy(currentTasks))
            Fmin = math.inf
            iterator = 0
            binIterator = 0
            for binChar in reversed(binTasksToCheck):
                if binChar == '1':
                    binChecking = list(reversed(binTasksToCheck))
                    binChecking[binIterator] = '0'
                    binChecking.reverse()
                    cutBinChecking = []
                    for k in range(0, len(binChecking)):
                        if binChecking[k] == '1':
                            cutBinChecking = binChecking[k:len(binChecking)]
                            break
                    binChecking = ''.join(cutBinChecking)
                    
                    F = max((sumOfP - currentTasks[iterator][2]), 0) * currentTasks[iterator][1]
                    if binChecking in knownValues:
                        F += knownValues[binChecking]
                    if F < Fmin:
                        Fmin = F
                    iterator = iterator + 1
                binIterator = binIterator + 1
                    
            knownValues[binTasksToCheck] = Fmin
        currentTasks.clear()
    return Fmin
        
def pSum(zad):
    sum = 0
    for i in range(0, len(zad)):
        sum += zad[i][0]
    return sum

def dynamicRecursionStart(zad):
    availableTasks = copy.deepcopy(zad)
    currentTasks = []
    knownValues = {}
    Fmax = math.inf
    n = len(zad)
    binTasksToCheck = "1" * n

    def dynamicRecursion(zad, current, binChecking):
        nonlocal Fmax
        nonlocal n
        availableTasks = copy.deepcopy(zad)
        currentTasks = copy.deepcopy(current)
        
        if len(zad) != 0 and currentTasks != n:
            for i in range(0, len(availableTasks)):
                binChecking = list(binChecking)
                binChecking[availableTasks[i][3]-1] = '0'
                binChecking = ''.join(binChecking)
                if binChecking not in knownValues:
                    currentTasks.append(copy.copy(availableTasks[i]))
                    temp = availableTasks.pop(i)
                    dynamicRecursion(availableTasks, currentTasks, binChecking)
                    availableTasks.insert(i, temp)
                binChecking = list(binChecking)
                binChecking[availableTasks[i][3]-1] = '1'
                binChecking = ''.join(binChecking)
                currentTasks.pop()
        else:
            F = calculate_Fmax(copy.deepcopy(currentTasks))
            knownValues[binChecking] = F
            print(F)
            if F < Fmax:
                Fmax = F

    dynamicRecursion(availableTasks, currentTasks, binTasksToCheck)
    return Fmax

zadania = loadData("data/data3.txt")
#print(calculate_Fmax(copy.deepcopy(zadania)))
#zadaniaSortD = sortD(copy.deepcopy(zadania))
#print(calculate_Fmax(copy.deepcopy(zadaniaSortD)))
#print(optPermutations(copy.deepcopy(zadania)))
#print(optRecursionStart(copy.deepcopy(zadania)))

print(dynamicIterations(copy.deepcopy(zadania)))
print(dynamicRecursionStart(copy.deepcopy(zadania)))
