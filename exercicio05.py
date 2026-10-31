
print("Cadastrar nome, idade e altura de 3 pessoas")

pessoas = {}

for i in range(3):
    nome = input(f"{i+1}º Nome: ")
    idade = int(input(f"{i+1}ª Idade: "))
    altura = float(input(f"{i+1}ª Altura: "))

    pessoas[nome] = {'idade': idade, 'altura': altura}

print(f"Dicionário completo: {pessoas}")
