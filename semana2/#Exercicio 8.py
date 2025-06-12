#Exercicio 8
#Conversor de médidas.

#variaavel recebe valor atravez de um input previamente convertido para FLOAT.
valor = float(input('Digite uma distancia em metros: '))


print('O ' + str(valor) +'m em kilometro é: ' + str(float(valor)/1000) + "km.")
print('O ' + str(valor) +'m em hectômetro é: ' + str(float(valor)/100) + "hm.")
print('O ' + str(valor) +'m em decâmetro é: ' + str(float(valor)/10) + "dam.")
print('O ' + str(valor) +'m em decimetro é: ' + str(int(valor)*10) + "dm.")
print('O ' + str(valor) +'m em centimetro é: ' + str(int(valor)*100) + "cm.")
print('O ' + str(valor) +'m em milimetro é: ' + str(int(valor)*1000) + "mm.")
