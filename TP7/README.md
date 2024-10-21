# Relatório do TPC do TP7
## Data: 21-10-2024
## Autor: Mariana Alves A107205

## Resumo

O TPC do TP7 consistiu na criação de uma aplicação de metereologia.
Considerei que o modelo da lista de dias registados tem a seguinte estrutura:
    TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
        Data = (Int,Int,Int)
        TempMin = Float
        TempMax = Float
        Precipitacao = Float

No menu da aplicação existem as operações:
- (0) Criar uma tabela metereológica
- (1) Média das temperaturas máxima e mínima
- (2) Guardar a tabela em ficheiro
- (3) Carregar uma tabela dum ficheiro
- (4) Consultar a temperatura mínima mais baixa
- (5) Calcular a amplitude das temperaturas diárias
- (6) Consultar a precipitação máxima
- (7) Consultar os dias com precipitação superior a x
- (8) Consultar o número de dias consecutivos em que a precipitação teve valores inferiores a x
- (9) Criar um gráfico com temperetauras máxima, mínima e pluviosidade
- (10) Sair da aplicação

No fim de executar a operação selecionada, a aplicação coloca novamente o menu e pede ao utilizador uma nova opção para continuar.
Iniciei por definir todas as funções necessárias e posteriormente adiciona-las ao menu.