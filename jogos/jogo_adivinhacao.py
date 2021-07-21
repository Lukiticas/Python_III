import random 
def jogar_Ad():
    rein = True
    while rein:
        numero_secreto = round(random.randrange(1,101))
        print(numero_secreto)
        total_de_tentativas = 0
        chances = 0
        pontos = 1000

        print("***********************")
        print("bem vindo ao adivinhações!!")
        print("***********************", "\n")

        print("Qual o nivel da dificuldade?")
        print("(1) Fácil, (2) Médio, (3) Difícil")

        nivel = int(input("Define o nivel: "))
        if nivel == 1:
            total_de_tentativas = 20 
            chances = 20
        elif nivel == 2:
            total_de_tentativas = 10
            chances = 10
        else:
            total_de_tentativas = 5
            chances = 5

        for rodada in range(0, total_de_tentativas):
            print("==tentativa {} de {}==".format(total_de_tentativas, chances))

            chute = int(input("Adivinhe um número entre 1 e 100: "))

            if chute < 1 or chute >= 100:
                print("Digite um valor valido!!")
                continue 

            acertou = numero_secreto == chute
            maior = numero_secreto < chute
            menor = numero_secreto > chute  

            if acertou:
                print("Você acertou e fez {} pontos!!".format(pontos))
                break
            else:
                total_de_tentativas -= 1
                if maior:
                    print("você errou! o seu chute foi bem alto eih!!",)
                elif menor:
                    print("você errou! o seu chute foi bem baixo eih!!",)
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

            if total_de_tentativas < 1:
                print("\nAcabou suas tentativas!")
                print("o numero secreto era {}, mas mesmo assim você fez {} pontos".format(numero_secreto, pontos))
        
        if acertou or total_de_tentativas < 1:
            print("************")
            print("fim de jogo")
            jogar_denovo = int(input("Quer jogar de novo?\n(1)sim (0)nao"))
            if jogar_denovo == 1:
                continue
            else:
                break

if __name__ == "__main__":
    jogar_Ad()
            

