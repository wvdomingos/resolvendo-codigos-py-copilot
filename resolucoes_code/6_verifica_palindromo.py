# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Remove espaços e converte para minúsculas
palavra = palavra.replace(" ", "").lower()

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se é um palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
