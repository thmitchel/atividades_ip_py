jogador_votado1 = input("Digite o primeiro jogador: ")
pais_jurado1 = input("Digite o pais do primeiro jurado: ").lower()
votos1 = 0

if(jogador_votado1 == "rodri" and pais_jurado1 == "espanha"):
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")
    votos1 = 0

elif(jogador_votado1 == "vinijr" and pais_jurado1 == "brasil"):
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")
    votos1 = 0

else:
    print("Voto registrado!")
    votos1 = 1

jogador_votado2 = input("Digite o segundo jogador: ")
pais_jurado2 = input("Digite o pais do segundo jurado: ").lower()
votos2 = 0

if(jogador_votado2 == "rodri" and pais_jurado2 == "espanha"):
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")
    votos2 = 0

elif(jogador_votado2 == "vinijr" and pais_jurado2 == "brasil"):
    print("Voto inválido! Não é permitido votar em jogadores do mesmo país.")
    votos2 = 0

else:
    print("Voto registrado!")
    votos2 = 1

if(jogador_votado1 == "rodri"):
    print(f"Votos válidos para rodri: {votos1}")

elif(jogador_votado1 == "vinijr"):
    print(f"Votos válidos para vinijr: {votos1}")

if(jogador_votado2 == "rodri"):
    print(f"Votos válidos para rodri: {votos2}")

elif(jogador_votado2 == "vinijr"):
    print(f"Votos válidos para vinijr: {votos2}")
