#TPC5
## Gerir um cinema

from datetime import date

def menu():
    cinema = [] #variavel interna
    v = True
    while v == True:
        print("""MENU:
(1) Inserir sala
(2) Listar filmes
(3) Disponibilidade de lugar
(4) Editar salas
(5) Vender bilhete
(0) Sair do programa""")
        
        modo = int(input("Seleciona o modo pretendido"))
        
        if modo == 1:
            inserir_sala(cinema)
        elif modo == 2:
            if len(cinema) == 0:
                print("Não existem salas registadas")
            else:
                listar_filmes(cinema)
        elif modo == 3:
            if len(cinema) == 0:
                print("Não existem salas registadas")
            else:
                listar_disponibilidade(cinema)
        elif modo == 4: 
            if len(cinema) == 0:
                print("Não existem salas registadas")
            else:
                editar_sala(cinema)
        elif modo == 5:
            if len(cinema) == 0:
                print("Não existem salas registadas")
            else:
                vender_bilhetes(cinema)
        elif modo == 0:
            print("Programa Encerrado")
            v = False
        else:
            print("Insere um modo válido")

#Inserir sala
def inserir_sala(cinema):
    s = int(input("Insere o número de salas que pretendes adicionar"))
    #len(cinema) = s
    while s > 0:
        sala = []

        print ("Adicionar nova sala")

        num_lugares = int(input("Número de lugares? "))
        lugares = list(range(1, num_lugares + 1))
        sala.append(lugares)

        vendidos = 0
        sala.append(vendidos)

        filme = str(input("Insere o nome do filme em exibição"))
        sala.append(filme)

        s -= 1
        cinema.append(sala)

#Listar filmes
def listar_filmes(cinema):
    if len(cinema) == 0:
        print("Não existem salas registadas")
    else:
        i = 1
        for sala in cinema:
            print(f"Sala{i} - Filme: {sala[2]}")
            i += 1

#Disponibilidade de lugar
def listar_disponibilidade(cinema):
    if len(cinema) == 0:
        print("\nAtualmente não há salas.")
    else:
        i = 1
        for sala in cinema:
            print(f"""Sala{i}
- Filme: {sala[2]} 
- Lugares: {len(sala[0])}""")
        contador_lugar = 0
        for lugar in sala[0]: 
                print(lugar, end=' ') 
                contador_lugar += 1
                if contador_lugar % 10 == 0:
                    print()
        print(f"""
- Bilhetes vendidos: {sala[1]}
- Lugares disponiveis: {len(sala[0]) - sala[1]}""")

#Editar salas
def editar_sala(cinema):
    v = True
    while v == True:
        print("""(1) Mudar nome do filme 
(2) Remover Filme 
(0) Voltar ao Menu""")
        
        modo = int(input("Que modo deseja?"))

        if modo == 1:
            i = int(input(f"Qual sala pretendes editar? (1 a {len(cinema)})")) -1
            cf = input(f"Tens a certeza que pretendes editar o filme em exibição na sala {i + 1}? (s/n)")
            if cf == "s":
                cinema[i][2] = str(input("Nome do filme"))
                print("Filme alterado!")
            else:
                print("Número da sala inválido.")
        
        elif modo == 2:
            i = int(input(f"Qual sala pretendes editar? (1 a {len(cinema)})")) -1
            cf = input(f"Tens a certeza que pretendes remover o filme em exibição na sala {i + 1}? (s/n)")
            if cf == "s":
                cinema[i][2] = str("Sem filmes em exibição")
                print("Filme removido!")
            else:
                print("Voltar ao Menu")
                v = False
        
        elif modo == 0:
            print("Voltando ao menu")
            v = False
        else:
            print("Insere um modo válido")

# Vender Bilhetes
def vender_bilhetes(cinema):
    i = int(input(f"Escolhe uma sala (1 a {len(cinema)})")) -1
    if not cinema[i][2] == "Sem filmes em exibição":
        v = int(input("Quantos bilhetes queres comprar?"))
        if 0 <= i < len(cinema):
            sala = cinema[i]
            if len(sala[0]) - sala [1] > v:
                sala[1] += v
            else:
                print("Não é possível comprar esse número de bilhetes na sala que pretendes")
            contador_lugar = 0
            for lugar in sala[0]:
                print(lugar, end=" ")
                contador_lugar += 1
                if contador_lugar % 10 == 0:
                    print()
            while v > 0:
                lugar = int(input("Que lugar deseja?"))
                if lugar in cinema[i][0]:
                    contador_numero = 0
                    for numero in cinema[i][0]:
                        if numero == lugar:
                            cinema[i][0][contador_numero] = "(-)"
                            v -= 1
                        contador_numero += 1
                else:
                    print("Esse lugar já está ocupado.")
        cinema[i][1] += v
    else:
        print("Sala sem filme!")

menu()