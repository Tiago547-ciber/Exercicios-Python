
#EXERCICIO 12

#LOJA SUPER COMPRA

#SISTEMA DE CDESCONTOS AUTOMÁTICOS

def desc(valor):
    
    if valor <= 100.00:
        return valor-valor*0.05
    elif valor <= 500.00:
        return valor-valor*0.15
    else:
        print("Valor fora da cobertura de descontos.")
        return valor-valor*0
        
def super():
    on = 1
    while on == 1:
        print("SUPERMERCADO SUPER COMPRA.")
        print("BEM VINDO AO SISTEMA DE PAGAMENTO.")
        print("DIGITE O VALOR A SER PAGO.")
        valorP = float(input("R$ "))
        
        parcelar = input("Deseja parcelar?")
        if parcelar == "sim" or parcelar == "SIM":
            print("DESEJA PARCELAR EM QUANTAS VEZES?")
            quantParcela = int(input("ATÉ 10X: "))
            print(str(valorP) + " PARCELADO EM " + str(quantParcela) + "X: " + str(valorP/quantParcela))
            print("Deseja fazer um novo pagamento? ")
            resp = input("SIM OU NÃO?")
            
            if resp == "NÃO" or resp == "não":
                print("ATÉ A PROXIMA!")
                return on == 0
            else:
                ""
        b = desc(valorP)
        
        print("CLIENTE OBTEVE DESCONTO! O total a ser pago é: R$" + str(b) + ".")
        print(" ")
        print("Deseja fazer um novo pagamento? ")
        resp = input("SIM OU NÃO?")
        
        if resp == "NÃO" or resp == "não":
            print("ATÉ A PROXIMA!")
            return on == 0
        else:
            ""
super()