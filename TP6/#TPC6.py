#Aplicação para gestão de alunos


def menu():
    v = True
    turma = []
    while v == True:
        print("""MENU: 
(1) Criar uma turma
(2) Inserir um aluno na turma
(3) Listar a turma
(4) Consultar um aluno por id
(5) Guardar a turma em ficheiro
(6) Carregar uma turma dum ficheiro
(0) Sair da aplicação """)
        modo = int(input("Introduz o modo que pretendes realizar:"))
        if modo == 1:
            criar_turma(turma)
        elif modo == 2:
            if len(turma) == 0:
                print("Não é possível realizar este comando, porque não existe nenhuma turma criada")
            else:
                print("Inserir aluno na turma:")
                inserir_aluno(turma)
        elif modo == 3:
            if len(turma) == 0:
                print("Não é possível realizar este comando, porque não existe nenhuma turma criada")
            else:
                print("Listar turma:")
                list_turma(turma)
        elif modo == 4:
            if len(turma) == 0:
                print("Não é possível realizar este comando, porque não existe nenhuma turma criada")
            else:
                procurar_id(turma)
        elif modo == 5:
            if len(turma) == 0:
                print("Não é possível realizar este comando, porque não existe nenhuma turma criada")
            else:
                guardar_turma(turma)
        elif modo == 6:
            if len(turma) == 0:
                print("Não é possível realizar este comando, porque não existe nenhuma turma criada")
            else:
                recuperar_turma()
        elif modo == 0:
            print("Aplicação Terminada")
            v = False
        else:
            print("Modo Inválido")    



#aluno = (nome, id, [notaTPC, notaProj, notaTeste])
#turma = [aluno]

## Criar Turma
def criar_turma(turma):
    nalunos = int(input("Quantos alunos pretendes adicionar à turma?"))
    while nalunos > 0:
        aluno = []

        nome = str(input("Inserir nome do aluno"))
        aluno.append(nome)
    
        id = str(input("Insere o id dom aluno(A____)"))
        aluno.append(id)

        notaTPC = float(input("Insere a nota do TPC"))
        notaProj = float(input("Insere a nota do Projeto"))
        notaTeste = float(input("Insere a nota do Teste"))
        aluno.append([notaTPC, notaProj, notaTeste])

        nalunos -= 1
        turma.append(tuple(aluno))

#Inserir um aluno na turma´+
def inserir_aluno(turma):
    aluno = []

    nome = str(input("Inserir nome do aluno"))
    aluno.append(nome)
    
    id = str(input("Insere o id dom aluno(A____)"))
    aluno.append(id)

    notaTPC = float(input("Insere a nota do TPC"))
    notaProj = float(input("Insere a nota do Projeto"))
    notaTeste = float(input("Insere a nota do Teste"))
    aluno.append([notaTPC, notaProj, notaTeste])

    turma.append(tuple(aluno))

#Listar turma
def list_turma(turma):
    print(turma)

#Consultar um aluno por id
def procurar_id(turma):
    id = str(input("Insere o id do aluno que pretende procurar(A____)"))
    v = True
    while v == True:
        for aluno in turma:
            if aluno[1] == id:
                print (aluno)
                v = False
            else:
                print("Não existe nenhum aluno com esse id")

#Guardar a turma em ficheiro
def guardar_turma(turma):
    file = open("turma_criada.txt", "w")
    for aluno in turma:
        for t in aluno:
            notas = str(aluno[2][0]) + "," + str(aluno[2][1]) + "," + str(aluno[2][2])
            linha = str(aluno[0]) + "::" + str(aluno[1]) + "::" + notas + "\n"
            file.write(linha)
    file.close()

#Carregar uma turma dum ficheiro 
##Voltar ao formato de lista de tuplos
def recuperar_turma():
    turma = []
    aluno = []
    file = open("turma_criada.txt", "r")
    for linha in file:
        if linha != "":
            termos = linha.split("::")
            aluno.append((str(termos[0]), str(termos[1])))
            for t in aluno[2]:
                campos = t.split(",")
                aluno.append([float(campos[0]), float(campos[1]), float(campos[2])])
    turma.append(aluno)

menu()