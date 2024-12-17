# Vamos calcular a média de três notas fornecidas na entrada do usuário

def calcular_media():

    try:
        # Solicitação de entrada do usuário e armazenamento em variáveis
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        nota3 = float(input("Digite a 3ª nota: "))

        # Cálculo da média usando operadores aritméticos
        media = (nota1 + nota2 + nota3) / 3

        # Exibição do resultado da média
        print(f"A média das notas é: {media:.2f}")

        # Verificação de aprovação ou reprovação
        if media >= 7:
            print("Situação: Aprovado! 🎉")
        else:
            print("Situação: Reprovado. 😔")

    except ValueError:
        # Tratamento de erro caso a entrada não seja um número válido
        print("Erro: Por favor, digite valores numéricos para as notas.")

# Chamada da função
calcular_media()
