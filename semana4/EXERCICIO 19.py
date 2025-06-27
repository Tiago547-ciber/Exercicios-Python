#EXERCICIO 19

#IMPORTANDO BIBLIOTECA


import random

#FUNÇÃO QUE RETORNA VALOR RANDOMICAMENTE

def aleatorio(grupo):
# recebe uma array com nomes e retorna um valor randomicamente.
    return random.choice(grupo)


def interact():

    print("Digite o nome dos alunos: ")

    alunos = input()

    grupo = alunos.split(",")

    print("O aluno escolhido para apresentar foi: " + aleatorio(grupo))

interact()    