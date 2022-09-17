#Faça um programa que olhe todos os itens de uma lista e diga quantos deles
são pares.

#entradas da lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#guarda as quantidades
somador = 0

#percorre os valores da lista
for num in lista:
    if num % 2 == 0:
        somador += 1

    else: somador += 0
#imprime os valores
print("A quantidade de n°s pares são: ", somador)

