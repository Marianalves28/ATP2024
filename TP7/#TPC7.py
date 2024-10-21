#TPC7
## Aplicação Metereológica

def criarTabMeteo(t):
    ndias = int(input("Insere o número de dias que pretendes registar"))
    while ndias > 0:
        dia = []
        ano = int(input("Insere o ano do registo"))
        mes = int(input("Insere o mes do registo"))
        ddia = int(input("Insere o dia do registo"))
        dia.append((ano,mes,ddia))
        tmin = float(input("Insere a temperatura mínima registada"))
        tmax = float(input("Insere a temperatura máxima registada"))
        precip = float(input("Insere a precipitação registada"))
        dia.append(tmin, tmax, precip)
        ndias -= 1
        t.append(tuple(dia))
    return

def medias(t):
    res = []
    for dia in t:
        med = (dia[1] + dia[2]) / 2
        res.append((dia[0], med))    
    return res

def guard(t):
    file = open("meteorologia.txt", 'w')
    for linha in t:
            linha = str(linha[0][0]) + "::" + str(linha[0][1]) + "::" + str(linha[0][2]) + "::" + str(linha[1]) + "::" + str(linha[2]) + "::" + str(linha[3]) + "\n"
            file.write(linha)
    file.close()
    print("Ficheiro guardado!")
    return

def carreg():
    res = []
    file = open("meteorologia.txt")
    for linha in file:
        if linha !="":
            campos = linha.split('::')
            data = (int(campos[0]), int(campos[1]), int(campos[2]))
            res.append((data, float(campos[3]), float(campos[4]), float(campos[5])))
    return res

def minMin(t):
    min = t[0][1]
    for _,tmin,_,_ in t[1:]: 
        if tmin < min:
            min = tmin
    return min

def amplTerm(t):
    res = []
    for dia in t:
        amp = dia[2] - dia[1]
        res.append((dia[0], amp))
    return res 

def maxChuva(t):
    maxp =t[0][3]
    maxd =t[0][0]
    for data,_,_,precip in t[1:]: 
        if maxp < precip:
            maxp = precip
            maxd = data
    return ((maxd, maxp))

def diasChuvosos(t):
    p = float(input("Insere o valor de x"))
    res = []
    for data,_,_,precip in t: 
        if precip > p:
            res.append([data, precip])
    return res

def maxPeriodoCalor(t):
    p = float(input("Insere o valor de x"))
    res = 0
    consecutivos = 0
    for _,_,_,precip in t:
        if precip < p:
            res += 1
            if res > consecutivos:
                consecutivos = res
        else:
            res = 0
    return consecutivos

def gra(t):
    import matplotlib.pyplot as plt
    # x pluviosidade
    # y t
    x1 = []
    y1 = []
    x2 = []
    y2 = [] 
    for _,tmin,tmax,precip in t:
        #Linha 1
        y1.append(float(precip))
        x1.append(int(tmin))
        #linha2
        y2.append(float(precip))
        x2.append(int(tmax))

    plt.plot(x1, y1, label = "linha 1 - tmin")
    plt.plot(x2, y2, label = "linha 2 - tmax")
    plt.xlabel('Temperatura')
    plt.ylabel('Pluviosidade')
    plt.title('Gráfico Temperaturas/Pluviosidade')
    plt.legend()
    plt.show()
    return


def menu():
    v = True
    t = []
    while v == True:
        print("""--------MENU------
(0) Criar uma tabela metereológica
(1) Média das temperaturas máxima e mínima
(2) Guardar a tabela em ficheiro
(3) Carregar uma tabela dum ficheiro
(4) Consultar a temperatura mínima mais baixa
(5) Calcular a amplitude das temperaturas diárias
(6) Consultar a precipitação máxima
(7) Consultar os dias com precipitação superior a x
(8) Consultar o número de dias consecutivos em que a precipitação teve valores inferiores a x
(9) Criar um gráfico com temperetauras máxima, mínima e pluviosidade
(10) Sair da aplicação""")
        op = int(input("Introduz o a opção que pretendes executar"))
        if op == 0:
            criarTabMeteo()
        elif op == 1:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Média das temperaturas máxima e mínima")
                medias(t)
        elif op == 2:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Guardar a tabela em ficheiro")
                guard(t)
        elif op == 3:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Carregar uma tabela dum ficheiro")
                carreg()
        elif op == 4:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Consultar a temperatura mínima mais baixa")
                minMin(t)
        elif op == 5:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Calcular a amplitude das temperaturas diárias")
                amplTerm(t)
        elif op == 6:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Consultar a precipitação máxima")
                maxChuva(t)
        elif op == 7:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Consultar os dias com precipitação superior a x")
                diasChuvosos(t)
        elif op == 8:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Consultar o número de dias consecutivos em que a precipitação teve valores inferiores a x")
                maxPeriodoCalor(t)
        elif op == 9:
            if t == []:
                print("Não existem  dados para executar a tarefa!")
            else:
                print("Criar um gráfico com temperetauras máxima, mínima e pluviosidade")
                gra(t)
        elif op == 10:
            print("Sair da Aplicação!")
            v = False
        else:
            print("Opção inválida!")
    return

menu()