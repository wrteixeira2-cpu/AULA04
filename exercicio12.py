
# Função para calcular o INSS
def calcular_inss(salario):
    if salario >= 1800:
        return salario * 0.11
    else:
        return salario * 0.09


# Função para calcular o vale-transporte
def calcular_vale(salario):
    if salario >= 1500:
        return salario * 0.06
    else:
        return salario * 0.05


# Função para calcular o bônus
def calcular_bonus(salario):
    if salario >= 1240:
        return 700
    else:
        return 500


# Função para definir o cargo
def definir_cargo(salario):
    if salario >= 3000:
        return "Acionista"
    elif salario >= 2000:
        return "Gerente"
    else:
        return "Vendedor"


# Função para calcular o salário líquido
def calcular_liquido(salario, inss, vale, bonus):
    return salario - (inss + vale) + bonus


# Programa principal
nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário bruto: R$ "))

inss = calcular_inss(salario)
vale = calcular_vale(salario)
bonus = calcular_bonus(salario)
cargo = definir_cargo(salario)

liquido = calcular_liquido(salario, inss, vale, bonus)


# Exibindo os resultados
print("\n===== FOLHA DE PAGAMENTO =====")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R$ {salario:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Vale-transporte: R$ {vale:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Cargo: {cargo}")
print(f"Salário líquido: R$ {liquido:.2f}")
