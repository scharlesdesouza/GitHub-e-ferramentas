# Solicitar uma string e um número inteiro como entrada. Depois retornar a string a quantidade de vezes informada contento espaçamento entre as strings

string = input("Digite uma String: ")

try:
    numero = int(input("Digite um número inteiro: "))
    print((string + ' ') * numero)
except ValueError:
    print("Erro: Você deve digitar um número inteiro válido.")
