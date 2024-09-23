# TPC TP2
## Modalidade 1
from random import randint
computador = randint(0, 100)
jogador = int(input("Em que número pensei?")) 
tentativas = 0

while jogador != computador:
    if jogador < computador:
        print("O número que pensei é Maior")
        jogador = int(input("Em que número pensei?")) 
        tentativas = tentativas + 1
    elif jogador > computador:
        print("O número que pensei é Menor")
        jogador = int(input("Em que número pensei?"))
        tentativas = tentativas + 1 

tentativas = tentativas + 1
print(f"Acertou em {tentativas} tentativas")

## Modalidade 2
print("Pensa num número de 0 a 100, se eu não acertar diz me se o número é maior ou menor.")
min = 0
max = 100
tentativas = 0
palpite = int((min + max)/2)
print(palpite)
resposta = input("avalia o meu palpite")

while resposta != "acertou":
    if resposta == "maior":
        min = palpite + 1
        palpite = int((min + max)/2)
        print(palpite)
        resposta = input("avalia o meu palpite")
        tentativas = tentativas + 1
    elif resposta == "menor":
        max = palpite - 1
        palpite = int((min + max)/2)
        print(palpite)
        resposta = input("avalia o meu palpite")
        tentativas = tentativas + 1
tentativas = tentativas + 1
print (f"Acertei em {tentativas} tentativas")
