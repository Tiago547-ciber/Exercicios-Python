#Exercicio 9
#TABUADA


#Um valor é atribuido a uma variavel atravez de um input.
num = input("Digite um número: ")

#Uma variavel CONT recebe o valor 0 que será incrementado atravez de um laço WHILE.
cont = 0


print("A tabuada de " + num + " é: ")

#Quando o laço é ativado, ele soma o valor atual de CONT + 1,
#em seguida  multiplica o valor de NUM pelo valor atual de CONT.
while  cont < 10:
    cont = cont + 1
    print(num + " x " + str(cont) + " = " + str(int(num)*int(cont)))