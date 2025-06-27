#EXERCICIO 18

#O SISTEMA RECEBE UM VALOR DE ANGULO E RETORNA SENO COSENO E TANGENTE

#IMPORTANDO BLIBLIOTECA 

from math import sin, cos, tan, radians, ceil

#DEFININDO FUNÇÕES QUE RETORNARÃO OS VALORES

def seno(sen):
    return sin(sen)

def coseno(cose):
    return cos(cose)

def tangente(tang):
    return tan(tang)

def interact():
    print("Digite o valor de um angulo: ")

    num = int(input())
    resp = radians(num)
    print("O SENO de " + str(num) + " é: " + str(ceil(seno(resp)*10)/10))
    print("O COSENO de " + str(num) + " é: " + str(ceil(coseno(resp)*10)/10))
    print("A TANGENTE de " + str(num) + " é: " + str(ceil(tangente(resp)*10)/10))

interact()    