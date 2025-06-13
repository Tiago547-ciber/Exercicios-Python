#Exercicio 14

#CONVERSOR DE TEMPERATURA

def fahrenheit(temperatura):
    return temperatura * 33.8
    
def kelvin(temperatura):
    return temperatura * 274.15    
    
    
#INTERFACE DE INTERAÇÃO

def conversor():
    print("CONVERSOR DE MEDIDAS.")
    
    
    on = 1
    #ENQUANTO ON CONTIVER O VALOR 1, O LOOP IRA CONTINUAR.
    while on == 1:
        valor = float(input("Digite um valor para ser convertido: "))
        
        print("Deseja converter para qual mendida?")
        resp = int(input("1 - FAHRENHEIT / 2 - KELVIN"))
        
        if resp == 1:
            result = fahrenheit(valor)
            print(str(valor) + "C° equivale a " + str(f"{result:3f}") + "F°")
            
            cont = input("Deseja continuar?")
            
            if cont == "não":
                print("Até a proxima!")
                return on == 0
            else:
                return conversor()  
        if resp == 2:
            result = kelvin(valor)
            print(str(valor) + "C° equivale a " + str(f"{result:3f}") + "F°")
             
            cont = input("Deseja continuar?")
            
            if cont == "não":
                print("Até a proxima!")
                return on == 0
            else:
                return conversor()          
conversor()        
   