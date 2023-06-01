import random
import math

menor_num = int(input("Digite o menor número: "))
maior_num = int(input("Digite o maior número: "))

num_aleatorio = random.randint(menor_num, maior_num)
tentativas = round(math.log(maior_num - menor_num + 1, 2))
print(f"Você tem {tentativas} tentativas para acertar o número!")

contador = 0

while contador < tentativas:
    contador += 1
    palpite = int(input("Adivinhe o número: "))

    if num_aleatorio == palpite:
        print("Parabéns! Você acertou o número.")
        break
    elif num_aleatorio > palpite:
        print("Tente novamente! O número escolhido foi muito baixo.")
    elif num_aleatorio < palpite:
        print("Tente novamente! O número escolhido foi muito alto.")

if contador >= tentativas:
    print(f"O número era: {num_aleatorio}")
    print("Mais sorte na próxima vez!")
