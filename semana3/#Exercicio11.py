#EXERCICIO 11

#CRIAR UMA FUNÇÃO QUE RECEBA AS MEDIDAS DE ALTURA, LARGURA
#E RETORNE A AREA DA PAREDE E QUANTO DE TINTA SERÁ NECESSARIO PARA PINTAR.


#DEFININDO A FUNÇÃO PINTOR

def pintor():
    

    print("Bem vindo ao assistênte de pintura.")
    print("Primeiro preciso de duas informações.")
    
    #AS INFORMAÇÕES SÃO ARMAZENADAS NAS VARIAVEIS.
    largura = float(input("Qual a largura da parede?"))
    altura = float(input("Qual a altura da parede?"))

    #CRIAMOS UMA VARIAVEL QUE RECEBE A MULTIPLICAÇÃO DOS VALORES
    area = largura*altura

    #VARIAVEL QUANTTINTAS recebe o valor da area/2*1
    
    quantTinta = float(area/2*1)

        
    #OS VALORES SÃO RETORNADOS AO CLIENTE
    print("A sua parede de " + str(largura) + "x" + str(altura))
    print("e mede " + str(area) + "m² e precisa de " + str(quantTinta) + "L.")

pintor() 