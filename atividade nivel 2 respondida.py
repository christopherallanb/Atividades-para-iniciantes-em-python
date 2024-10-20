### Exercício 1

#Crie um programa que classifique uma pessoa em uma das seguintes categorias com base na idade:

#*   Criança (0-12 anos)
#*   Adolescente (13 a 17 anos)
#*   Adulto (18-64 anos)
#*   Idosos (65 anos ou mais)  

idade = int(input("Informe sua idade: "))
if idade <= 0:
    print("Idade inválida")
elif idade <= 12: 
    print ("Criança")
elif idade <= 17:
    print ("Adolescente")
elif idade <= 64:
    print ("Adulto")
else:
    print ("Idosos")
#### Exercício 2

#Implemente um programa que calcule o desconto aplicado em uma compra, considerando as seguintes regras:

#*   Se o valor da compra for maior ou igual a `$100`, será aplicado um desconto de `10%`.
#*   Se o valor da compra for maior ou igual a `$200`, será aplicado um desconto de `20%`.

compras = float(input ('valor das compras'))
desconto1 = compras / 100 * 10
desconto2 = compras /100 * 20
if compras <=100:
    valor = compras - desconto1
    print (valor)
elif compras >= 200:
    valor = compras - desconto2
    print (valor)


### Exercício 3

#Crie um programa que determine o tipo de triângulo (equilátero, isósceles ou escaleno) com base no comprimento de seus lados.
lado1 = float(input('digite o lado 1: '))
lado2 = float(input('digite o lado 2: '))
lado3 = float(input('digite o lado 3: '))
def tipo_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return 'equilátero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return 'isósceles'
        else:
            return 'escaleno'
    else:
        return 'não é um triângulo'
print(tipo_triangulo(lado1, lado2, lado3))



### Exercício 4
#Crie um programa que classifique as notas de um aluno em duas disciplinas e imprima se o aluno for aprovado em ambas as disciplinas.

#*   O aluno é aprovado se obtiver nota igual ou superior a 60 em cada disciplina.
#*   Caso o aluno falte em alguma delas, poderá realizar exame de nivelamento. Se for o caso, imprima que deve fazer a prova da disciplina específica.
#*   Se perder ambas, deverá imprimir reprovado.

#A faixa de pontuação é de 0 a 100.

def main():
    nota1 = float(input('Digite a nota da primeira disciplina (0-100): '))
    nota2 = float(input('Digite a nota da segunda disciplina (0-100): '))
    def verificar_aprovacao(nota1, nota2):
        if nota1 >= 60 and nota2 >= 60:
            return "Aprovado em ambas as disciplinas."
        elif nota1 < 60 and nota2 < 60:
            return "Reprovado em ambas as disciplinas."
        else:
            if nota1 < 60:
                return "Deve fazer prova de nivelamento na disciplina 1."
            if nota2 < 60:
                return "Deve fazer prova de nivelamento na disciplina 2."
    print(verificar_aprovacao(nota1, nota2))
main()


### Exercício 5

#Crie um programa no qual o computador escolhe um número aleatório entre 1 e 100 e depois pede ao usuário que adivinhe o número. Fornece pistas que indicam se o número a ser adivinhado é maior ou menor. Use um loop `while` até que o usuário adivinhe corretamente.
    

import random
akinator = random.randint(1, 100)
akinator2 = int(akinator)
jogador = int(input('tente adivinhar o número de 1 a 100: '))
if jogador == akinator2:
    print('acertou')
else:
    print('errou')
    while True:
        if jogador > akinator2:
            print('tente um número menor')
        elif jogador < akinator2:
            print('tente um número maior')
        jogador = int(input('tente adivinhar o número de 1 a 100: '))
        if jogador == akinator2:
            print('acertou')
            break

### Exercício 6

#Escreva um programa que conte o número de vogais de uma palavra digitada pelo usuário. Ele usa um loop `for` para iterar cada caractere da palavra.

palavra = input('Digite uma palavra: ')
vogais = ['a','e','i','o','u']
for letra in palavra:
    if letra in vogais:
        print(letra, end=' ')



### Exercício 7

#Projete um programa que simule as operações de um caixa eletrônico. Permite ao usuário fazer depósitos, saques e consultar saldo. Use loops `while` para manter a interação até que o usuário decida sair.

saldo_inicial = 1000.0
print("Bem-vindo ao banco!")
while True:
    print("Seu saldo atual é de R$", saldo_inicial)
    # Menu de opções
    print("1 = Saque")
    print("2 = Depósito")
    print("3 = Consultar saldo")
    print("4 = Sair")
    usuario = int(input("O que gostaria de fazer?: "))
    # Opção 4 - Sair
    if usuario == 4:
        print("Até logo!")
        break
    # Opção 1 - Saque
    if usuario == 1:
        valor_saque = float(input("Qual o valor do saque? "))
        if valor_saque > saldo_inicial:
            print("Você não tem saldo suficiente para realizar este saque.")
        else:
            saldo_inicial -= valor_saque
            print("Saque realizado com sucesso. Seu saldo atual é de R$", saldo_inicial)
    # Opção 2 - Depósito
    elif usuario == 2:
        valor_deposito = float(input("Qual o valor do depósito? "))
        saldo_inicial += valor_deposito
        print("Depósito realizado com sucesso. Seu saldo atual é de R$", saldo_inicial)
    # Opção 3 - Consultar saldo
    elif usuario == 3:
        print("Seu saldo atual é de R$", saldo_inicial)
    else:
        print("Opção inválida. Tente novamente.")
