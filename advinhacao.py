print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 13

chute_str = input("Digite o seu número: ")

print("você digitou " , chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou, parabéns!")
else:
    print("Você errou!")

print("Fim do jogo.")