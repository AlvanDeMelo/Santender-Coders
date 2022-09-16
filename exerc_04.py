#Pede os dados de entrada
mora = input("Mora perto da vítima? ")
trabalhou = input("Já trabalhou coma a vítima? ")
telefonou = input('Telefonou para a vítima? ')
local = input("Esteve no local do crime? ")
devia = input("Devia para a vítima? ")

somatoria = 0
#Analisa as respostas
contador = 0

if mora == 'sim':
    contador += 1
else: contador += 0

if trabalhou == 'sim':
   contador += 1
else: contador += 0

if telefonou == 'sim':
   contador += 1
if local == 'sim':
   contador += 1
else: contador += 0
