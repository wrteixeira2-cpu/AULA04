
alunos = {}

for i in range(3):
    nome = input(f"Digite o {i+1}º Nome: ")
    notas = {}

    for j in range(3):
        nota = float(input(f"Digite a {j+1}ª Nota: "))
        notas[f"nota{1+j}"] = nota

    media = sum(notas.values()) / len(notas)

    alunos[nome] = {
        "notas": notas,
        "media": media
    }

print("\n===== RESULTADO FINAL =====\n")

for nome, dados in alunos.items():
    print(f"Aluno: {nome}")
    print(f"Notas: {dados['notas']}")
    print(f"Média: {dados['media']:.2f}")
    print("---------------------------")
