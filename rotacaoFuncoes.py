# Funcoes:
# Lixo: [0:6]
# Area: [6:10]
# Bosta: [10:13]
# Panos: [13:16]
from colorama import Fore, Back, Style


def printFuncoes(lista):
    print("Lixo:  ", lista[0:6])
    print("Area:  ", lista[6:10])
    print("Bosta: ", lista[10:13])
    print("Pano:  ", lista[13:16])


def printNovasFuncoes(base, nova):
    print(Fore.WHITE, "Lixo:  ", end="")
    for i in range(0, 6):
        if base[i] in nova[0:6]:
            print(Fore.RED, nova[i], end="")
        else:
            print(Fore.GREEN, nova[i], end="")
    print()
    print(Fore.WHITE, "Area:  ", end="")
    for i in range(6, 10):
        if base[i] in nova[6:10]:
            print(Fore.RED, nova[i], end="")
        else:
            print(Fore.GREEN, nova[i], end="")
    print()
    print(Fore.WHITE, "Bosta: ", end="")
    for i in range(10, 13):
        if base[i] in nova[10:13]:
            print(Fore.RED, nova[i], end="")
        else:
            print(Fore.GREEN, nova[i], end="")
    print()
    print(Fore.WHITE, "Pano:  ", end="")
    for i in range(13, 16):
        if base[i] in nova[13:16]:
            print(Fore.RED, nova[i], end="")
        else:
            print(Fore.GREEN, nova[i], end="")
    print()


def troca(funcoes):
    novasFuncoes = []
    for i in range(0, 16):
        novasFuncoes.append(i)
    novasFuncoes[6:9] = funcoes[0:3]
    novasFuncoes[10:12] = funcoes[3:5]
    novasFuncoes[13] = funcoes[5]
    novasFuncoes[3] = funcoes[9]
    novasFuncoes[4] = funcoes[13]
    novasFuncoes[5] = funcoes[15]
    novasFuncoes[12] = funcoes[6]
    novasFuncoes[14] = funcoes[7]
    novasFuncoes[15] = funcoes[8]
    novasFuncoes[0] = funcoes[10]
    novasFuncoes[1] = funcoes[11]
    novasFuncoes[2] = funcoes[14]
    novasFuncoes[9] = funcoes[12]

    return novasFuncoes


def printTroca(moradores, funcoesAtuais):
    print(Fore.WHITE, "Lixo:\t\t ", end="")
    for i in range(0, 6):
        print(Fore.RED, moradores[funcoesAtuais[i]], end="")
    print()
    print(Fore.WHITE, "Area Externa:\t ", end="")
    for i in range(6, 10):
        print(Fore.GREEN, moradores[funcoesAtuais[i]], end="")
    print()
    print(Fore.WHITE, "Bosta do Napo:\t ", end="")
    for i in range(10, 13):
        print(Fore.BLUE, moradores[funcoesAtuais[i]], end="")
    print()
    print(Fore.WHITE, "Panos e Louças: ", end="")
    for i in range(13, 16):
        print(Fore.LIGHTMAGENTA_EX, moradores[funcoesAtuais[i]], end="")
    print()


def line():
    print("------------------------------------------------------------")


moradores = ["Michelas", "Bide", "Ita", "Dante", "Kagawa", "PVC", "BeyBlade",
             "Alceu", "Shot", "Ronaldao", "Bilu", "t", "Perda", "Miles", "Marqteto", "Matheus"]
funcoes = [[]]
for i in range(0, len(moradores)):
    funcoes[0].append(i)
novasFuncoes = funcoes.copy()


def trocaNVezes(n: int, funcoes):
    #n = (n % 4) + 1
    for i in range(1, n):
        #print(f"Funções: {i}")
        funcoes.append(troca(funcoes[i-1]))
        print(f"Semana: {i}")
        printTroca(moradores, funcoes[i-1])
        #printNovasFuncoes(funcoes[i-1], funcoes[i])
    return funcoes[n-1]
    # printFuncoes(funcoes[i])
# printFuncoes(funcoes)
#novasFuncoes1 = troca(funcoes)


##printTroca(moradores, novasFuncoes1)
funcao = trocaNVezes(8, funcoes)
