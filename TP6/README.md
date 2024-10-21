# Relatório do TPC do TP6
## Data: 14-10-2024
## Autor: Mariana Alves A107205

## Resumo

O TPC do TP6 consistiu na criação de uma aplicação de gestão de alunos.
Considerei que o modelo do aluno e da turma têm a seguinte estrutura:

aluno = (nome, id, [notaTPC, notaProj, notaTeste])
turma = [aluno]

No menu da aplicação existem as operações:
- 1: Criar uma turma
- 2: Inserir um aluno na turma
- 3: Listar a turma
- 4: Consultar um aluno por id
- 8: Guardar a turma em ficheiro
- 9: Carregar uma turma dum ficheiro
- 0: Sair da aplicação

No fim de executar a operação selecionada, a aplicação coloca novamente o menu e pede ao utilizador a opção para continuar.
Iniciei por definir todas as funções necessárias e posteriormente adiciona-las ao menu.