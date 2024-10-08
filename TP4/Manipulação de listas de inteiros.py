# TPC P4
# Aplicação para manipulação de lista de inteiros

## Defenição das funções a usar

def criarLista():
    import random
    lista = []
    i = 0
    N = int(input('Quantos números pretende ter na sua lista?'))
    while i < N:
        lista.append(random.randint(1, 100))
        i = i + 1
    return lista

def leLista():
    lista = []
    i = 1
    N = int(input('Quantos números pretende ter na sua lista?'))
    while i <= N:
        lista.append(int(input(f'Introduz o número {i}/{N} da tua lista')))
        i = i + 1
    return lista

def somaLista(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    return soma

def mediaLista(lista):
    soma = 0
    i = 0
    while i < len(lista):
        soma = soma + lista[i]
        i = i + 1
    media = soma/len(lista)
    return media

def maiorLista(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

def menorLista(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
             menor = num
    return menor

def estaOrdenadaCrescente(lista):
    res = True
    i = 0
    while res == True and i < len(lista) -1 :
        if lista[i] >= lista [i + 1]:
            res = False
        else:
            i += 1
    return res

def estaOrdenadaDecrescente(lista):
    res = True
    i = 0
    while res == True and i < len(lista) -1 :
        if lista[i] <= lista [i + 1]:
            res = False
        else:
            i += 1
    return res

def procurarLista(lista):
    res = []
    i = 0
    elem = int(input("Introduz o número que pretendes procurar"))
    for num in lista:
        if num == elem:
            res.append(i)
        else:
            i += 1
    if res == []:
        res = [-1]
    return res

def menu():
    print("""Vamos manipular uma lista de inteiros, podes realizar as seguintes operações.
(1) Criar Lista 
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair""")


## Aplicação

opcao = -1
listaGuardada = []
while opcao != "0":
    menu()
    opcao = input ("Introduz o número correspondente à opção que pretendes realizar")
    if opcao == "1":
        listaGuardada = criarLista()
        print(listaGuardada)
    elif opcao == "2":
        listaGuardada = leLista()
        print(listaGuardada)
    elif opcao == "3":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(somaLista(listaGuardada))
    elif opcao == "4":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(mediaLista(listaGuardada))
    elif opcao == "5":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(maiorLista(listaGuardada))
    elif opcao == "6":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(menorLista(listaGuardada))
    elif opcao == "7":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(estaOrdenadaCrescente(listaGuardada))
    elif opcao == "8":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(estaOrdenadaDecrescente(listaGuardada))
    elif opcao == "9":
        if listaGuardada == []:
            print("É necessário criar uma lista antes de realizar esta operação. Para isso seleciona 1 ou 2 no menu.")
            menu()
        else:
            print(procurarLista(listaGuardada))
    elif opcao not in ("0123456789"):
        print("Opção desconhecida")
print(listaGuardada)
print("Obrigada, volte sempre!")