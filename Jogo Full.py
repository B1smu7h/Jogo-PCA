

def start():
    print("Você e um soldado robotico na força especial de defesa da Terra chamada de 'Mathmech'")
    print("Atualmente você se encontra dentro de sua base, que se localiza na orbita da Terra.")
    print("Por conta de um alarme codigo vermelho, você pega seus dois armamentos especiais, as armas de 'Adição' e Subtração'")
    print("Na sua frente você tem somente um caminho, aquele que leva diretamente ate o inimigo.")
    input("Aperte 'ENTER' para prosseguir.")
    encontro1()

def encontro1():
    print("")
    print("")
    print("No Hangar da base, você ve alguns de seus aliados ja lutando contra o inimigo, um Mecha que parece ser da facção rival, os 'Mekk-Knights'.")
    print("Você se aproxima e se prepara para ajudar seus aliados!")
    print("Iniciando seu sistema de combate, você encontra 3 escudos que se forem desabilitados, o inimigo ira cair junto.")
    print("Por sorte, você tem as armas necessarias para acertar eles!")
    print("TUTORIAL: Para danificar seu inimigo, você precisa acertar qual e o valor marcado como '?' na conta que mantem o escudo dele.")
    print("Escudo 1: 16 + ? = 64")
    atk = input("Coordenadas de ataque: ")
    if atk == "48":
        encontro1pt2()
    else:
        print("")
        print("O ataque errou!")
        encontro1()

def encontro1pt2():
    print("")
    print("Primeiro escudo derrubado!")
    print("Escudo 2: (47 + ?) + 86 = 169")
    atk = input("Coordenadas de ataque: ")
    if atk == "36":
        encontro1pt3()
    else:
        print("")
        print("O Ataque errou!")
        encontro1pt2()

def encontro1pt3():
    print("")
    print("Segundo escudo derrubado!")
    print("Ultimo Escudo! = (32 + 98) - 30 = ?")
    atk = input("Coordenadas de Ataque: ")
    if atk == "100":
        encontro1clear()
    else:
        print("")
        print("O Ataque Errou!")
        encontro1pt3()

def encontro1clear():
    print("")
    print("Com esse ultimo ataque, o Mecha inimigo e desativado! Permitindo vocês e seus alidos a interrogarem ele para saber o motivo desse ataque.")
    print('Inimigo: "Eu não sei de muita coisa por conta da minha patente, mas eu sei de uma base proxima que esta se preparando para fazer um segundo ataque a essa localização."')
    print("Escutando essa informação, você e alguns de seus aliados se preparam para dar um contra ataque nessa base proxima.")
    print("Você pega os armamentos mais pesados, e viaja pelo espaço até chegar nessa base inimiga.")
    input("Aperte 'ENTER' para prosseguir.")
    encontro2()

def encontro2():
    print("")
    print("Você e seus aliados chegam na base inimiga com uma entrada explosiva e barulhenta, e em pouco tempo, vocês estão sob ataque de mais Mechas inimigos!")
    print("Rapidamente, você ativa seu modo de combate.")
    print("Cada um de seus aliados escolhe um Mecha e começa combate, o ultimo que restou se aproxima de você, rapidamente, você visualiza seus escudos.")
    print("Escudo 1: (25 + 30) - (15 + 10) = ?")
    atk = input("Coordenadas de Ataque: ")
    if atk == "30":
        encontro2pt2()
    else:
        print("")
        print("O Ataque Errou!")
        encontro2()

def encontro2pt2():
    print("")
    print("Acerto em Cheio!")
    print("Segundo Escudo: 7 * 9 = ?")
    atk == input("Coordenadas de Ataque: ")
    if atk == "63":
        print("")
        encontro2pt3()
    else:
        print("")
        print("O ataque errou!")
        encontro2pt2()

def encontro2pt3():
    print("")
    print("Acerto em cheio!")
    print("Terceiro Escudo: 156 + ? = 743")
    atk == input("Coordenadas de Atk: ")
    if atk == "743":
        print("")
        print("Inimigo Derrotado!")
    else:
        print("")
        print("O ataque Errou!")
        encontro3()


def encontro3():
    print("")
    print("Apos derrotar esse inimigo, você e seus aliados se juntam para atacar o ultimo Mecha dessa base! Ele parece mais resistente, Mas com os armamentos de todos seus aliados, não deve ser um problema!")
    print("Ataque combinado!: (7 x (14 - 11) + 9) / 2 = ?  ")
    atk = input("Coordenadas do Ataque: ")
    if atk == "15":
        print("")
        final()
    else:
        prit("")
        print("O ataque falhou!")
        encontro3()

def Final():
    print("Com esse ultimo inimigo derrotado, Vocês e seus aliados conseguem por a base para se auto-destruir!")
    print("Vitoria!")
    print("Obrigado por jogar!")
    exit()

start()