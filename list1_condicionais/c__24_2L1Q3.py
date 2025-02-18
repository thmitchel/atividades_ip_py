nome_jogador1 = input('Digite o primeiro indicado: ').lower()
pontuacao_jogador1 = int(input('Digite a pontucao do primeiro indicado: '))

nome_jogador2 = input('Digite o segundo indicado: ').lower()
pontuacao_jogador2 = int(input('Digite a nota do segundo indicado: '))

nome_jogador3 = input('Digite o terceiro indicado: ').lower()
pontuacao_jogador3 = int(input('Digite a nota do terceiro indicado: '))


if(pontuacao_jogador1 > pontuacao_jogador2 > pontuacao_jogador3 and nome_jogador1 == "rodri"):
    print("O melhor jogador do mundo é {nome_jogador1}, com {pontuacao_jogador1} ponto(s). Os europeus, como sempre, roubaram o nosso ouro!")

elif(pontuacao_jogador1 > pontuacao_jogador2 > pontuacao_jogador3 and nome_jogador1 == "vini"):
    print("O melhor jogador do mundo é {nome_jogador1}, com {pontuacao_jogador1} ponto(s). Os brasileiros amaram o resultado! BAILA VINI!")

elif(pontuacao_jogador1 > pontuacao_jogador2 > pontuacao_jogador3):
    print("O melhor jogador do mundo é {nome_jogador1}, com {pontuacao_jogador1} ponto(s). Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!")

elif(pontuacao_jogador2 > pontuacao_jogador3 and nome_jogador2 == "rodri" ):
    print("O melhor jogador do mundo é {nome_jogador2}, com {pontuacao_jogador2} ponto(s). Os europeus, como sempre, roubaram o nosso ouro!")

elif(pontuacao_jogador2 > pontuacao_jogador3 and nome_jogador2 == "vini" ):
    print("O melhor jogador do mundo é {nome_jogador2}, com {pontuacao_jogador2} ponto(s). Os brasileiros amaram o resultado! BAILA VINI!")

elif(pontuacao_jogador2 > pontuacao_jogador3):
    print("O melhor jogador do mundo é {nome_jogador2}, com {pontuacao_jogador2} ponto(s). Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!")

elif(pontuacao_jogador1 < pontuacao_jogador2 < pontuacao_jogador3 and nome_jogador3 == "rodri"):
    print("O melhor jogador do mundo é {nome_jogador3}, com {pontuacao_jogador3} ponto(s). Os europeus, como sempre, roubaram o nosso ouro!")

elif(pontuacao_jogador1 < pontuacao_jogador2 < pontuacao_jogador3 and nome_jogador3 == "vini"):
    print("O melhor jogador do mundo é {nome_jogador3}, com {pontuacao_jogador3} ponto(s). Os europeus, como sempre, roubaram o nosso ouro!")

else:
    print("O melhor jogador do mundo é {nome_jogador3}, com {pontuacao_jogador3} ponto(s). Essa premiação perdeu o sentido mesmo, como que o Vini Jr. não ganhou? Muito roubado!")
