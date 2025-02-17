plateia1 = input("Digite o primeiro da plateia: ").lower()
plateia2 = input("Digite o segundo da plateia: ").lower()
vencedor = input("Digite o vencedor: ").lower()

if(vencedor == "palé"):
    print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")

elif(vencedor == "maodona" and (plateia1 == "gaviao bonito" or plateia1 == "ronaldinho paulista") and (plateia2 == "gaviao bonito" or plateia2 == "ronaldinho paulista")):
    print("Acabou!!! o Brasil faz a festa e a paz no mundo é selada! PALÉ É O MELHOR DO MUNDO!")

elif(vencedor == "maodona" and (plateia1 == "gaviao bonito" or plateia2 == "gaviao bonito")):
    print("Gavião soltou seu grito, mas não foi o suficiente para dar o troféu ao rei do fut. Triste dia para o futebol mundial…")

elif(vencedor == "maodona" and (plateia1 == "ronaldinho paulista" or plateia2 == "ronaldinho paulista")):
    print("Paulista subiu no palco sozinho e ninguém sabe o porquê. Mais um momento aleatório e mais um dia triste para o brasileiro…")

elif(vencedor == "maodona" and plateia1 != "gaviao bonito" and plateia2 != "ronaldinho paulista"):
    print("PERDEMOS! O futebol foi roubado e não há mais chance de volta por enquanto")

else:
    print("Não foi dessa vez, mas pelo menos não perdemos a nossa dignidade.")
