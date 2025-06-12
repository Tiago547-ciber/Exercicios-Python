#Exercicio 13

#Avaliar aumento de salario

#DEFININDO FUNÇÃO AVALIADORA DE PORCENTAGEM DE AUMENTO
def aval(tempo):
    if tempo <= 2:
        return 0.05
    elif tempo <= 5:
        return 0.10
    else:
        return 0.15


#DEFININDO FUNÇÃO QUE APLICA O AUMENTO
on = True
def promo():
    while on == True:
            print("HORA DE PROMOVER!")
            print("Responda 3 questões para avaliar o possivel aumento de salario.")
            
            quest1 = input("FUncionario entrega mais do que é solicitado no dia a dia?")
            quest2 = input("Funcionario desempenhou demonstra perfil proativo no dia a dia da equipe?")
            quest3 = input("FUncionario desempenha bem sua transversal?")
            

            if quest1 == "sim" and quest2 == "sim" and quest3 == "sim":
                 print("Ótimo, o funcionario entrega o esperado para a promoção.")
                 quest4 = int(input("Quantos anos de empresa o funcionario tem?"))
                  
                 salario = float(input("QUal o salario atual do funcionario?"))
                 novoSalario = salario + salario*aval(quest4)
                 print("O novo salario do funcionario é: " + str(float(f"{novoSalario:3f}")))

                 cont = input("Deseja avaliar outro funcionario?")

                 if cont == "não" or cont == "não":
                      print("Até a proxima!")
                      return on == False
            elif quest1 == "não" and quest2 == "sim" and quest3 == "sim":
                 print("Ótimo, o funcionario entrega 2 dos 3 itens necessarios para a promoção.")
                 print("O funcionario no momento não está apto para receber a promoção mais deve ser ACOMPANHADO POR UM MENTOR.")  
                 print("REFAÇA o teste em 6 MESES.")

                 cont = input("Deseja avaliar outro funcionario?")
                 if cont == "não" or cont == "não":
                      print("Até a proxima!")
                      return on == False
            elif quest1 == "sim" and quest2 == "não" and quest3 == "sim":
                 print("Ótimo, o funcionario entrega 2 dos 3 itens necessarios para a promoção.")
                 print("O funcionario no momento não está apto para receber a promoção mais deve ser ACOMPANHADO POR UM MENTOR.")  
                 print("REFAÇA o teste em 6 MESES.")

                 cont = input("Deseja avaliar outro funcionario?")                 
                 if cont == "não" or cont == "não":
                      print("Até a proxima!")
                      return on == False  
            elif quest1 == "sim" and quest2 == "sim" and quest3 == "não":
                 print("Ótimo, o funcionario entrega 2 dos 3 itens necessarios para a promoção.")
                 print("O funcionario no momento não está apto para receber a promoção mais deve ser ACOMPANHADO POR UM MENTOR.")  
                 print("REFAÇA o teste em 6 MESES.")

                 cont = input("Deseja avaliar outro funcionario?")                 
                 if cont == "não" or cont == "não":
                      print("Até a proxima!")
                      return on == False  
            else:
                 print("ATENÇÃO! O funcionario entrega  apenas 1 item necessarios para a promoção ou não entrega nenhum item.")
                 print("O funcionario no momento não esta apto para receber a promoção.")
                 print("REFAÇA o teste em 6 MESES.")

                 cont = input("Deseja avaliar outro funcionario?")                 
                 if cont == "não" or cont == "não":
                      print("Até a proxima!")
                      return on == False                  

promo()
