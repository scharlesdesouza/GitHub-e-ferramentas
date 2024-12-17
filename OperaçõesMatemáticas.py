# Solicitar dois números inteiros como entrada e depois realizar uma operação simples entre eles.

# Função para verificar entrada de número inteiro
def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor  # Retorna o valor se for um número inteiro
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")

# Entrada dos números inteiros
num1 = ler_inteiro("Digite o 1° número inteiro: ")
num2 = ler_inteiro("Digite o 2° número inteiro: ")

# Entrada da operação desejada
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Estrutura condicional para realizar as operações
if operacao == '+':
    print(f"Resultado: {num1 + num2}")
elif operacao == '-':
    print(f"Resultado: {num1 - num2}")
elif operacao == '*':
    print(f"Resultado: {num1 * num2}")
elif operacao == '/':
    # Tratamento adicional para divisão por zero
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Erro: Operação inválida.")
