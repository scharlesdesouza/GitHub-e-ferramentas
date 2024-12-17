# Vamos testar se uma palavra é um palíndromo?! Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

def verificar_palindromo():
    
    # Entrada da palavra fornecida pelo usuário
    palavra = input("Digite uma palavra para verificar se é um palíndromo: ").lower().replace(" ", "")

    # Inversão da palavra
    palavra_invertida = palavra[::-1]

    # Comparação entre a palavra original e a invertida
    if palavra == palavra_invertida:
        print(f"A palavra '{palavra}' é um palíndromo!")
    else:
        print(f"A palavra '{palavra}' NÃO é um palíndromo.")

verificar_palindromo()
