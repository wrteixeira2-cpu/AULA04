
# Função de soma
def somar(a, b):
    return a + b

# Função de subtração
def subtrair(a, b):
    return a - b

# Função de multiplicação
def multiplicar(a, b):
    return a * b

# Função de divisão
def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero!"
    return a / b


# Programa principal
print("=== CALCULADORA ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == 1:
    resultado = somar(num1, num2)
    print(f"Soma: {resultado}")

elif opcao == 2:
    resultado = subtrair(num1, num2)
    print(f"Subtração: {resultado}")

elif opcao == 3:
    resultado = multiplicar(num1, num2)
    print(f"Multiplicação: {resultado}")

elif opcao == 4:
    resultado = dividir(num1, num2)
    print(f"Divisão: {resultado}")

else:
    print("Opção inválida!")
