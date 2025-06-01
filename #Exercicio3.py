#Exercicio 3
#Criar função para executar soma.


def soma():
     #Primeiro declaramos duas variaveis com input, para armazenar os valores.
     input1 = input("Digite um numero: ")
     input2 = input("Digite um numero: ")

     #Convertemos os inputs de string para integer armazenando em novas variaveis.
     numero1 = int(input1)
     numero2 = int(input2)

      #Somase os numeros
     soma = numero1 + numero2

     #converter o resultado de volta para string.

     result = str(soma)

     #O resultado é retornado ao usuario.

     print("O resultado da soma é: " + result)

soma()