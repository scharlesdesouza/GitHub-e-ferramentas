# Receber um número inteiro e verificar se ele é par ou ímpar, utilizando IA para a resolução do problema

numero = input("Digite um número inteiro: ")

if numero.isdigit():  # Verifica se a entrada contém apenas dígitos
    numero = int(numero)  # Converte a entrada para inteiro
    if numero % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")
else:
    print("Entrada inválida! Por favor, digite um número inteiro.")
