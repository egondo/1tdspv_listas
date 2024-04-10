#Escreva um programa que recebe um número inteiro representando um cpf
#e imprime cada um dos dígitos.
#Por exemplo, se cpf = 23430938107, vai aparecer na tela os seguintes dígitos:
#7, 0, 1, 8, 3, 9, 0, 3, 4, 3, 2
import os

os.system("clear")  #os.system("cls") -> windows
cpf = int(input("Informe o CPF: "))
resp = ""

while cpf != 0:
    dig = cpf % 10
    resp = resp + str(dig) + ', '
    cpf = cpf // 10

print(resp)


