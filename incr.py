# Imprime os números de 1 a 20, excluindo o 13
for numero in range(1, 21):
    if numero != 13:
        print(numero)

        # Inicializa o contador
numero = 1

# Enquanto o número for menor ou igual a 20
while numero <= 20:
    # Se o número não for 13, imprime-o
    if numero != 13:
        print(numero)
    # Incrementa o contador
    numero += 1

    # Imprime os números de 20 a 1, excluindo o 13
for numero in range(20, 0, -1):
    if numero != 13:
        print(numero)

# Inicializa o contador com 20
numero = 20

# Enquanto o número for maior ou igual a 1
while numero >= 1:
    # Se o número não for 13, imprime-o
    if numero != 13:
        print(numero)
    # Decrementa o contador
    numero -= 1
    