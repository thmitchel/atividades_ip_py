#atributos primeiro jogador
nomej1 = input("Digite o nome do jogador 1: ").lower()
tnj1 = len(nomej1)
golsj1 = int(input("Digite o número de gols do jogador 1: "))
qpj1 = int(input("Digite o número de partidas do jogador 1: "))
vmj1 = float(input("Digite a velocidade máxima do jogador 1: "))
pf1 = ((golsj1 * 5) + (qpj1 * 2) + (vmj1 * 3)) / 10 + (tnj1 % 3)


#atributos segundo jogador
nomej2 = input("Digite o nome do jogador 2: ").lower()
tnj2 = len(nomej2)
golsj2 = int(input("Digite o número de gols do jogador 2: "))
qpj2 = int(input("Digite o número de partidas do jogador 2: "))
vmj2 = float(input("Digite a velocidade máxima do jogador 2: "))
pf2 = ((golsj2 * 5) + (qpj2 * 2) + (vmj2 * 3)) / 10 + (tnj2 % 3)

#atributos terceiro jogador
nomej3 = input("Digite o nome do jogador 3: ").lower()
tnj3 = len(nomej3)
golsj3 = int(input("Digite o número de gols do jogador 3: "))
qpj3 = int(input("Digite o número de partidas do jogador 3: "))
vmj3 = float(input("Digite a velocidade máxima do jogador 3: "))
pf3 = ((golsj3 * 5) + (qpj3 * 2) + (vmj3 * 3)) / 10 + (tnj3 % 3)

#-------------------------------------------------------------------------------#
#Condicionais

# Comparação para determinar a classificação
if pf1 > pf2 and pf1 > pf3:
    primeiro_nome, primeiro_pf = nomej1, pf1
    if pf2 > pf3:
        segundo_nome, segundo_pf = nomej2, pf2
        terceiro_nome, terceiro_pf = nomej3, pf3
    else:
        segundo_nome, segundo_pf = nomej3, pf3
        terceiro_nome, terceiro_pf = nomej2, pf2
elif pf2 > pf1 and pf2 > pf3:
    primeiro_nome, primeiro_pf = nomej2, pf2
    if pf1 > pf3:
        segundo_nome, segundo_pf = nomej1, pf1
        terceiro_nome, terceiro_pf = nomej3, pf3
    else:
        segundo_nome, segundo_pf = nomej3, pf3
        terceiro_nome, terceiro_pf = nomej1, pf1
else:
    primeiro_nome, primeiro_pf = nomej3, pf3
    if pf1 > pf2:
        segundo_nome, segundo_pf = nomej1, pf1
        terceiro_nome, terceiro_pf = nomej2, pf2
    else:
        segundo_nome, segundo_pf = nomej2, pf2
        terceiro_nome, terceiro_pf = nomej1, pf1

# Exibir a classificação
print(f"1 - {primeiro_nome} obteve {primeiro_pf:.2f} pontos.")
print(f"2 - {segundo_nome} obteve {segundo_pf:.2f} pontos.")
print(f"3 - {terceiro_nome} obteve {terceiro_pf:.2f} pontos.")

# Exibir o vencedor
print(f"{primeiro_nome} é o verdadeiro ganhador da Bola de Ouro com um total de {primeiro_pf:.2f} pontos.")