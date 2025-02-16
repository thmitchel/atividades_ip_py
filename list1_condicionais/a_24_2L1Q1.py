nome_jogador1 = input('Informe o primeiro jogador!: ').lower()
pontuacao1 = int(input('Informe a pontuacao do primeiro jogador: '))

nome_jogador2 = input('Informe o segundo jogador!: ').lower()
pontuacao2 = int(input('Informe a pontuacao do segundo jogador: '))

nome_jogador3 = input('Informe o terceiro jogador!: ').lower()
pontuacao3 = int(input('Informe a pontuacao do terceiro jogador: '))

#Utilização dos comandos condicionais

if(nome_jogador1 == "lucas lima" or nome_jogador2 == "lucas lima" or nome_jogador3 == "lucas lima"):
    print("Deu a lógica! Acabou caô, o Lucas Lima ganhoooouuu, Lucas Lima ganhoooouu oohhh!!!")

elif(pontuacao1 > pontuacao2 > pontuacao3):
    print(f"{nome_jogador1} é eleito o bola de ouro!")

elif(pontuacao2 > pontuacao1 > pontuacao3):
    print(f"{nome_jogador2} é eleito o bola de ouro!")

else:
    print(f"{nome_jogador3} é eleito o bola de ouro!")