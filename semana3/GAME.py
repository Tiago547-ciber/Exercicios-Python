
#GAME
def game():
    print("BEM VINDO AO JOGO DA ADIVINHAÇÃO!")
    resp = int(input("Digite um numero de 0 - 100"))
    
    if resp < 15:
        print("AHHH QUE PENA! VOCÊ ERROU! " + str(resp) + " É MENOR QUE A RESPOSTA CERTA!")
        cont = input("DESEJA TENTAR DE NOVO? SIM / NÃO")
        
        if cont == "SIM" or cont == "sim":
            print("VAMOS LÁ!")
            game()
        else:
            print("ATÉ A PROXIMA!")
    elif resp > 15:
        print("AHHH QUE PENA! VOCÊ ERROU! " + str(resp) + " É MAIOR QUE A RESPOSTA CERTA!")
        cont = input("DESEJA TENTAR DE NOVO? SIM / NÃO")
        
        if cont == "SIM" or cont == "sim":
            print("VAMOS LÁ!")
            game()
        else:
            print("ATÉ A PROXIMA!")
    else:
        print("PARABENS! RESPOSTA CERTA!")
        
game()