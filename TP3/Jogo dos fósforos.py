# Jogo dos fósforos:
## Menu
def menu():
    print("Vamos jogar ao jogo dos fósforos!")
    print("No início do jogo, há 21 fósforos; Cada jogador (computador ou utilizador), pode tirar 1, 2, 3 ou 4 fósforos quando for a sua vez de jogar.")
    print("Os jogadores jogam alternadamente; Quem tirar o último fósforo perde!")
    print("1. Começa a tirar os fósforos.")
    print("2. Começo eu a tirar fósforos.")
    print("3. Não quero jogar agora.")


## Modo 1
def modo_1():
    fosforos = 21
    while fosforos > 1:
        jog = int(input("Começas a tirar os fósforos, quantos queres tirar?"))
        print(f"Retiraste {jog} fósforos. Ficaram {fosforos - jog} fósforos.")
        fosforos = fosforos - jog
        comp  = 5 - jog
        print(f"Retirei {comp} fósforos. Ficaram {fosforos - comp} fósforos.")
        fosforos = fosforos - comp
    print("Perdeste. É a tua vez e sobra apenas 1 fósforo.")

## Modo 2
def modo_2():
    fosforos = 21
    while fosforos > 1:
        from random import randint
        comp = randint(1, 4)
        print(f"Retirei {comp} fósforos, restam {fosforos - comp} fósforos.")
        fosforos = fosforos - comp
        jog = int(input(f"Agora tu, quantos fósforos queres tirar?"))
        print(f"Retiraste {jog} fósforos. Ficaram {fosforos - jog} fósforos.")
        fosforos = fosforos - jog
        if jog + comp != 5:
            comp  = 5 - jog
            print(f"Retirei {comp} fósforos. Ficaram {fosforos - comp} fósforos.")
            fosforos = fosforos - comp
            jog = int(input(f" Agora tu, quantos fósforos queres tirar?"))
            print(f"Retiraste {jog} fósforos. Ficaram {fosforos - jog} fósforos.")
            fosforos = fosforos - jog
            while fosforos > 1:
                comp  = 5 - jog
                print(f"Retirei {comp} fósforos. Ficaram {fosforos - comp} fósforos.")
                fosforos = fosforos - comp
                jog = int(input(f" Agora tu, quantos fósforos queres tirar?"))
                print(f"Retiraste {jog} fósforos. Ficaram {fosforos - jog} fósforos.")
                fosforos = fosforos - jog
    print("Perdeste. É a tua vez e sobra apenas 1 fósforo.")

## Jogo ----------------------------------------------------------------

menu()
opcao = input ("Seleciona uma opção")
while opcao != "3":
    if opcao == "1":
        modo_1()
        repetir = input ("Queres voltar a jogar?")
        if repetir == "sim":
            menu()
        else:
            print("Obrigada, volte sempre!")
    elif opcao == "2":
        modo_2()
        repetir = input ("Queres voltar a jogar?")
        if repetir == "sim":
            menu()
        else:
            print("Obrigada, volte sempre!")
    else:
        print("Opção desconhecida")
print("Obrigada, volte sempre!")