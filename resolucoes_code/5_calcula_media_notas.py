# Solicitação das notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição do resultado formatado
print(f"A média das notas {nota1}, {nota2} e {nota3} é: {media:.2f}")
