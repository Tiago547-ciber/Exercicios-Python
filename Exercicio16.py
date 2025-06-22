# EXERCICIO 16
from math import floor

#DEFININDO FUNÇÃO PARA ARREDONDAMENTO

def turnUp(valor):
     return floor(valor)
     
     
#FUNÇÃO DE INTERAÇÃO

def interacao():
    
    valor = float(input("Digite um numero: "))
    valorConv = turnUp(valor)
    
    print("O valor digitado foi " + str(valor) + " e sua porção inteira é " + str(valorConv) + ".")
    
interacao()