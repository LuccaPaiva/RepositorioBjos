# Funcoes:
# Lixo Organico:   [0:2]
# Lixo Banheiro:   [2:4]
# Lixo Reciclavel: [4:6]
# Panos:           [6:8]
# Louça:           [8]
# Mesa cozinha:    [9]
# Sala:            [10:12]
# Ping Pong:       [12]
# Bosta:           [13:15]
# Extra:           [15]


from ast import Str
from cmath import inf
from typing import List
from numpy import void
from tabulate import tabulate


nomesMoradores = ["Michelas", "Bide", "Ita", "Kagawa", "PVC", "BeyBlade", "Alceu",
                  "Shot", "Ronaldao", "Bilu", "t", "Perda", "Miles", "Marqteto", "Edu"]

nomesFuncoes = {"Lixo Organico": [0, 1], "Lixo Banheiro": [2, 3], "Lixo Reciclavel": [4, 5],
                "Panos": [6, 7], "Louça": [8], "Mesa cozinha": [9], "Sala": [10, 11], "Ping Pong": [12],
                "Bosta": [13, 14]}
func = ["Lixo Organico", "Lixo Organico", "Lixo Banheiro", "Lixo Banheiro",
        "Lixo Reciclavel", "Lixo Reciclavel", "Panos", "Panos", "Louça", "Mesa cozinha",
        "Sala", "Sala", "Ping Pong", "Bosta", "Bosta"]

moradores = [[] for i in range(0, 15)]
moradores2 = [[] for i in range(0, 15)]
funcoes = [i for i in range(0, 15)]

#morador = [2, 5, 7]
#funcao = 13


def EstaNaLista(lista: List, conteudo: int):
    return lista.count(conteudo) > 0


def EstaOSuficiente(morador: List, funcoes: List, funcao: int):
    return morador.count(funcao) >= funcoes.count(funcao)


def MelhorCandidato(moradores, funcao: int, iteracao: int):
    contagem = []
    for i in range(0, len(moradores)):
        if len(moradores[i]) == iteracao + 1:
            contagem.append(float('inf'))
        else:
            contagem.append(moradores[i].count(funcao))
    #print(f"contagem: {contagem}")
    return contagem.index(min(contagem))


def Troca(moradores: List, funcoes: List):
    funcoesJaFeitas = []
    for morador in moradores:
        for funcao in funcoes:
            if not EstaOSuficiente(funcoesJaFeitas, funcoes, funcao):
                if not EstaNaLista(morador, funcao):

                    morador.append(funcao)
                    funcoesJaFeitas.append(funcao)
                    break


def Troca2(moradores: List, funcoes: list, iteracao: int):
    moradoreComFuncoes = []
    for funcao in funcoes:
        for i in range(0, len(moradores)):
            morador = MelhorCandidato(moradores, funcao, iteracao)
            # print(morador)
            if not EstaNaLista(moradoreComFuncoes, morador):
                #print(f"Morador {morador} faz {funcao}")
                moradores[morador].append(funcao)
                moradoreComFuncoes.append(morador)
                #print(f"Moradores Com: {moradoreComFuncoes}")
                break


def PrintEscala(n: int, moradores: List, nomeMoradores: List):
    print(tabulate(moradores, headers=[i for i in range(0, 15)]))
    print()


def PrintEscalaSemana(n: int, moradores: List, nomeMoradores=List):
    print(f"Escala: {n}")
    for morador in range(0, len(moradores)):
        print(f"{nomeMoradores[morador]}: {moradores[morador][n]}")
    print()


n = 9
for i in range(0, n):
    funcoesDaSemana = []
    Troca2(moradores2, func, i)
    #Troca(moradores, func)
    # print(moradores2)
PrintEscala(n, moradores2, nomesMoradores)
#PrintEscalaSemana(i, moradores, nomesMoradores)
