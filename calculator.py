import math


def sumnums(a, b):
    return a + b


def subnums(a, b):
    return a - b


def multnums(a, b):
    return a * b


def divnums(a, b):
    return a / b


def pot(b, e):
    return pow(b, e)


def squareRoot(a):
    return math.sqrt(a)


def percentage(a):
    return a * 100


print("\n-------------------CALCULADORA-------------------")

print(
    "1 - Soma\n"
    "2 - Subtração\n"
    "3 - Multiplicação\n"
    "4 - Divisão\n"
    "5 - Potência\n"
    "6 - Raíz quadrada\n"
    "7 - Percentagem"
)

op = int(input("\nEscolha uma operação: "))

if not 1 <= op <= 7:
    print("\nDeve escolher uma das operações mencionadas")
else:
    if 1 <= op <= 4:
        num1 = float(input("1º valor: "))
        num2 = float(input("2º valor: "))

        if op == 1:
            print(f'\n{num1} + {num2} = {sumnums(num1, num2)}')
        elif op == 2:
            print(f'\n{num1} - {num2} = {subnums(num1, num2)}')
        elif op == 3:
            print(f'\n{num1} * {num2} = {multnums(num1, num2)}')
        elif op == 4:
            print(f'\n{num1} / {num2} = {round(divnums(num1, num2), 2)}')

    elif op == 5:
        b = float(input("Base: "))
        e = float(input("Expoente: "))

        print(f'\n{b}^{e} = {pot(b, e)}')

    elif op == 6 or op == 7:
        num = float(input("Valor: "))

        if op == 6:
            print(f'\nRaíz quadrada de {squareRoot(num)}: ')

        elif op == 7:
            print(f'\nPercentagem: {int(percentage(num))}%')

