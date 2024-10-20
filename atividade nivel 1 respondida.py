

# 1.- Conversor de dias para segundos

# Peça ao usuário para inserir um número de dias e converta-o em segundos.

dias = int(input('quantos dias gostaria de converter para segundos?'))
segundos = dias * 86400
print('O número de segundos é:', segundos)

############################################################################

#**2.- Desconto em compras**

#Crie um programa que solicite ao usuário o valor total de sua compra. Aplique um desconto de 10% no total da compra. Imprima o valor após o desconto.

n1 = int(input("valor da compra: "))
n2 = n1 / 100 * 10
print("valor do desconto: ", n2)
print ("valor final: ", n1 - n2)

#############################################################################

#**3.- Conversão de moeda**

#Desenvolva um programa que converta uma quantia de dinheiro de dólares em euros. Solicite ao usuário o valor em dólares e a taxa de câmbio atual.

n1 = int(input("valor em dolares: "))
n2 = float(input("em dolares, quanto custa 1 euro hoje?: "))
euro = n2 * n1
resultado_simples = str(euro)[:4]
print(f"O valor em euros é: {resultado_simples}")

#############################################################################

#**4.- Anos de cachorro**

#Escreva um programa que solicite ao usuário a idade do seu animal de estimação e a converta em anos humanos. Imprima o resultado. Lembre-se de que 1 ano canino equivale a 7 anos humanos.

idade_cachorro =int (input("Qual a idade do cachorro? "))
n2 = 7
print("O cachorro tem", idade_cachorro * n2, "anos em idade humana")

#############################################################################

#**5.- Calculadora de Índice de Massa Corporal (IMC)**


#Escreva um programa que solicite ao usuário o peso (em quilogramas) e a altura (em metros) e calcule o IMC.

#IMC = peso / (altura ^ 2)

peso = float(input("Digite seu peso (em quilogramas): "))
altura = float(input("Digite sua altura (em metros): "))
imc = peso / (altura ** 2)
resultado_simples = str(imc)[:5]
print("Seu IMC é:", resultado_simples)

#############################################################################

#**6.- Hipotenusa**

#Desenvolva um programa que solicite ao usuário que insira os comprimentos dos dois catetos de um triângulo retângulo e calcule o comprimento da hipotenusa.

#Dica: Use a biblioteca matemática.

import math
cateto_1 = float(input("Por favor, digite o comprimento do primeiro cateto (em metros): "))
cateto_2 = float(input("digite o comprimento do segundo cateto (em metros): "))
hipotenusa = math.sqrt(cateto_1 ** 2 + cateto_2 ** 2)
print(f"\n  O comprimento da hipotenusa é aproximadamente: {hipotenusa:.2f} metros.")

#############################################################################

#**7.- Idade**

#Solicite ao usuário que insira sua data de nascimento e calcule sua idade.

#Dica: use a biblioteca datetime
from datetime import datetime
def calcular_idade(data_nascimento):
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year
    return idade
data_nascimento_input = input("Por favor, insira sua data de nascimento (dia-mês-ano): ")
try:
    data_nascimento = datetime.strptime(data_nascimento_input, "%d-%m-%Y")
    idade = calcular_idade(data_nascimento)
    print(f"Você tem {idade} anos.")
except ValueError:
    print("Formato de data inválido. Por favor, use dia-mês-ano.")
#forma muito mais simplificada =
# atual = int(2024)
# nasc = int(input("Qual o ano em que você nasceu? "))
#idade = atual - nasc
#print("Sua idade é: ", idade , " anos.")

#############################################################################

#**8.- Criação de e-mail**

#Solicite ao usuário que insira seu nome e sobrenome. Em seguida, gere um e-mail concatenando a inicial do nome com o sobrenome seguido de “@gmail.com”. O e-mail deve estar todo em letras minúsculas.

#Exemplo:

#nome: Gustavo

#Sobrenome: Lavadenz

#e-mail: glavadenz@gmail.com

nome = input("Insira seu nome: ")
sobrenome = input("Insira seu sobrenome: ")
email = f"{nome[0].lower()}{sobrenome.lower()}@gmail.com"
print("E-mail gerado:", email)

#############################################################################