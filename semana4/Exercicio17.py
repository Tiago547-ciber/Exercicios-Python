#EXERCICIO 17

#IMPORTANDO COMANDO SQRT DA BIBLIOTECA MATH

from math import sqrt

#CRIANDO FUNÇÃO PARA RETORNAR CALCUAR A HIPONENUSA.

def hip(cO, cA):
    hipotenuza = cO*cO+cA*cA
    return sqrt(hipotenuza)
    
    
    
#DEFININDO FUNÇÃO DE INTERAÇÃO

def interface():
    print("AUXILIAR DE CALCULO (HIPOTENUZA)")
    
    on = 1
    while on == 1:
        resp1 = float(input("Digite o valor do cateto oposto: "))
        resp2 = float(input("Digite o valor do cateto adjacente: "))
        
        print("o valor da hipotenuza é " + str(f"{hip(resp1, resp2): .2f}"))
        resp3 = input("Deseja continuar? ")
        
        if resp3 == "Não" or resp3 == "não" or resp3 == "n":
            print("até a próxima!")
            on = 0
            
interface()            
    