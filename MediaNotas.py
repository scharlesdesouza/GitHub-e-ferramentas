# Vamos calcular a média de três notas fornecidas na entrada do usuário

def calcular_media():
    """
    Função que solicita três notas ao usuário, calcula a média e exibe o resultado.
    """
    try:
        # Solicitação de entrada do usuário e armazenamento em variáveis
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        nota3 = float(input("Digite a 3ª nota: "))

        # Cálculo da média usando operadores aritméticos
        media = (nota1 + nota2 + nota3) / 3

        # Exibição do resultado
        print(f"A média das notas {nota1}, {nota2} e {nota3} é: {media:.2f}")

    except ValueError:
        # Tratamento de erro caso a entrada não seja um número válido
        print("Erro: Por favor, digite valores numéricos para as notas.")

# Chamada da função
calcular_media()