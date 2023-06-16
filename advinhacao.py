print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 13
total_de_tentativas = 3

while (total_de_tentativas > 0):
    print("tentativas: ", total_de_tentativas)
    chute_str = input("Digite o seu número: ")
    print("você digitou ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute< numero_secreto

    if (acertou):
        print("Você acertou, parabéns!")
    else:
        if (chute_maior):
            print("você errou!O chute foi maior que o número secreto.")
        elif(chute_menor):
            print("Você errou! O numero chutado foi menor que o número secreto.")

    total_de_tentativas = total_de_tentativas - 1

print("Fim do jogo.")
