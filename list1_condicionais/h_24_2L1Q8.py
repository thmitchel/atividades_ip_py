nomeJogador = input("Digite o nome do jogador: ")
qpj = int(input("Digite a quantidade de partidas jogadas pelo jogador: "))
qgm = int(input("Digite o número de gols do jogador: "))
qar = int(input("Digite a quantidades de assistências realizadas: "))
qdf = int(input("Quantidade de desarmes feitos: "))
liga = input("Informe da liga que participa o jogador: ")

#variáveis de variáveis
mediaGols = qgm / qpj
mediaAssistencia = qar / qpj
mediaDesarmes = qdf / qpj
score = [(qgm * 2) + (qar * 1) + (qdf * 0.4)]

if(liga == "Premier League"):
    score = [(qgm * 2) + (qar * 1) + (qdf * 0.4)]

elif(liga == "La Liga"):
    score = 0.95 * [(qgm * 2) + (qar * 1) + (qdf * 0.4)]

elif(liga == "Serie A"):
    score = 0.9 * [(qgm * 2) + (qar * 1) + (qdf * 0.4)]



if(liga != "Premier League" or "La Liga" or "Serie A" or "Brasileirão"):
    print(" liga informada não é válida ou o jogador não pertence a nenhuma das ligas elegíveis para a premiação.")

else:
    if(mediaGols < 0.3):
        print("O jogador está fora, não possui a média de gols necessária.")

    else:
        if(mediaAssistencia < 0.15):
            print("Infelizmente não teve assistências o suficiente, portanto não concorre ao prêmio.")

        else:
            if(mediaDesarmes < 1.25):
                print(f"{nomeJogador} não desarmou jogadores o suficiente, portanto está fora.")
            
            else:
                if(qpj < 50):
                    print("O atleta não jogou partidas o suficiente para concorrer à premiação.")
                
                else:
