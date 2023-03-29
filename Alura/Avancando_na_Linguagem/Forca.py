import random
def jogar():
    print_op_msg()

    palavra_chave = load_word()

    letras_acertadas = init_letters(palavra_chave)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Qual a letra? ").strip().upper()

        if chute in palavra_chave:         
            marca_chute(chute, palavra_chave, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Voce ganhou!")
    else:
        print("Voce perdeu!")

def print_op_msg():
    print("*********************************")
    print("***Bem_vindo ao jogo da forca!***")
    print("*********************************")

def load_word():
    arquivo =  open('Alura\Avancando_na_Linguagem\palavras.txt')
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip("\n"))

    arquivo.close()

    number = random.randrange(0,len(palavras))
    palavra_chave = palavras[number].upper()
    return palavra_chave

def init_letters(word):
    return ["_" for letra in word]
    

def marca_chute(chute, word, letras_acertadas):
    index = 0
    for letra in word:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index += 1

if __name__ == "__main__":
    jogar()