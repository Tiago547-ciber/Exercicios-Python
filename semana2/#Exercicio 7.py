#Exercicio 7
#Média aritimetica de um valor.

#Uma array contendo numeros é atribuido a uma variavel.
valor = [22, 33, 44, 57, 15]

#uma variavel chamada 'soma' recebe zero como valor
soma = 0


#Um laço FOR percorre os valores contendidos dentro da array,
#somando cada valor da array ao valor da variavel soma.
for variavel in valor:
    soma = soma+variavel

#O valor final da soma é dividido pelo numero de valores dentro da array,
#obtendo assim o valor da média.
print('A média do valor ' + str(soma/int(len(valor))))