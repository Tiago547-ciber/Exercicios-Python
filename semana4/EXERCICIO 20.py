#EXERCICIO 20

#IMPORTANDO BIBLIOTECA RANDOM

import random

#DEFININDO FUNÇÃO PARA RETORNAR VALOR ALEATORIO DENTRO DE ARRAY

def aleatorio(nomesS):         
     return random.choice(nomesS)

print("Digite  os quatro nomes dos componentes do grupo: ")


#os nomes são armazenados em uma variavel

nomes = input()

#uma variavel contem um array vazio onde serão inseridos os nomes dos componentes do grupo
#na ordem de apresentação.

grupo = []

#é criado uma array com os nomes separados utilizando o comando split
#a array é armazenada em uma nova variavel

nomesS = nomes.split(',')

#uma variavel é criada contendo o valor da quantidade de nomes dentro da array nomesS

cont = len(nomesS)


# com o valor de cont é criado um laço de repetição for
for i in range(cont):
     #para valor dentro da variavel cont;
     #1 A VARIAVEL NOME IRÁ RECEBER UM DOS NOMES DOS PARTICIPANTES ESCOLHIDOS ALEATORIAMENTE PELA FUNÇÃO ALEATORIO
     
     #2 SE O NOME NÃO ESTIVER ARMAZENADO NA ARRAY GRUPO
     #ENTÃO O NOME SERA INSERIDO E DEPOIS APAGADO DA ARRAY NOMESS

    
     nome = aleatorio(nomesS)

     if nome not in grupo:
          grupo.append(nome)
          nomesS.remove(nome)
          
                                                                                                                                              


print(grupo)
    



