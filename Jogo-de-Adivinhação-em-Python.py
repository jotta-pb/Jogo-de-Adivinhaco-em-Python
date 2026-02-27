print("--- Jogo de adivinhação ---\n")

import random

sorteio = random.randint(0,10)
tentativas = 0

while True:
    num = int(input("Estou pensando em um número entre 0 e 10, consegue adivinhar qual é ?\nResposta: "))
    
    if 0 < num <= 10 :
            
        while num != sorteio:
            if sorteio < num:
                num = int(input("Você errou! Tente um número menor.\nNúmero: "))
                tentativas += 1
                
            else:
                num = int(input("Você errou! Tente um número maior.\nNúmero: "))
                tentativas += 1
            
        if num == sorteio:
            print(f"\nVocê acertou! Eu pensei no número {sorteio} e você precisou de {tentativas} tentaivas!")
            break
        
    else:
        print("Somente entre 0 e 10! Tente novamente!\n")
