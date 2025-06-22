
def taxa(modelo):
    if (modelo == 2):
        return 200.00
    else:
        return 74.00


def AluguelC():
    on = True
    print("MOVE ON - ALUGUEL DE CARROS")
    

    while  on == True:
        print("Qual modelo de carro você pretende alugar?")
        
        tipo = input("Digite 1 - CARRO POPULAR / 2 - CARRO PLUS")
        modelo = taxa(tipo)
        
        print("Quantos dias pretende passar com o veiculo?")
        dias =   input("Dias: ") 
        
        print("o valor a ser pago é: " +str(float(modelo) * int(dias)))
        
AluguelC()        
        