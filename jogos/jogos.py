import jogo_forca
import jogo_adivinhacao

print("***********************")
print("bem vindo aos joguinhos!!")
print("***********************", "\n")

print("selecione o seu jogo!:")
print("(1) adivinhação!, (2) forca")

jogo = int(input("Qual jogo?: "))

if jogo == 1:
    print("jogando adivinhação!")
    jogo_adivinhacao.jogar_Ad()
elif jogo == 2:
    print("jogando forca!")
    jogo_forca.jogo_fc()