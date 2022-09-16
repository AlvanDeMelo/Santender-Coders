#Pede os dados de entrada
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
sexo = input('Digite o seu sexo: ')

#Analisa as entradas e imprime os valores
if idade <= 150:
    print("Idade OK!")
else: print("Reprovado na idade.")

if salario > 0:
    print("Salário OK!")
else: print("Reprovado no salário.")

if sexo == 'M':
    print("Sexo OK!")
elif sexo == 'F':
    print("Sexo OK!")
else: print("Faltou digitar o sexo.")
