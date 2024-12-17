# Receber um número inteiro e verificar se ele é par ou ímpar, utilizando IA para a resolução do problema

# Versão otimizada sugerida pela IA
numero = input("Digite um número inteiro: ")
print("Par" if numero.isdigit() and int(numero) % 2 == 0 else "Ímpar ou entrada inválida")
