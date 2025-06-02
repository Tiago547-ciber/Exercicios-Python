#Exercicio 4
#Criar uma função que verifique o tipo primitivo e todas as informações possiveis sobre a variavel.

info = input('Digite um nome: ')
print('O tipo primitivo desta variavel é: ' + str(type(info)))
print('Esta variavel contém apenas espaço em branco? '+ str(info.isspace()))          
print('Esta variavel é um numero? '+ str(info.isnumeric())) 
print('Contém apenas letras? ' + str(info.isalpha()))
print('É alfanumerico? '+ str(info.isalnum())) 
print('Contem apenas letras em Maiusculo? ' + str(info.isupper()))
print('Contém apenas letras em Minusculo? '+ str(info.islower()))
print(str(info.istitle())) 