taxa_fixa_empresa_1 = float(input("Digite a taxa fixa da empresa 1: "))
taxa_variavel_empresa_1 = float(input("Digite a taxa variável da empresa 1: "))

taxa_fixa_empresa_2 = float(input("Digite a taxa fixa da empresa 2: "))
taxa_variavel_empresa_2 = float(input("Digite a taxa variável da empresa 2: "))

#k = float(input("Digite a distancia em quilometros: "))
#P1 = (taxa_variavel_empresa_1 * k) + taxa_fixa_empresa_1
#P2 = (taxa_variavel_empresa_2 * k) + taxa_fixa_empresa_2

if(taxa_fixa_empresa_1 == taxa_fixa_empresa_2 and taxa_variavel_empresa_1 == taxa_variavel_empresa_2):
    print("As duas empresas tenhem o mesmo preço sempre!")

elif(taxa_variavel_empresa_1 == taxa_variavel_empresa_2):
    if(taxa_fixa_empresa_1 < taxa_fixa_empresa_2):
        print("A empresa 1 tem o melhor preço")
    else:
        print("A empresa 2 tem o melhor preço!")

elif(taxa_fixa_empresa_1 == taxa_fixa_empresa_2):
    if(taxa_variavel_empresa_1 < taxa_variavel_empresa_2):
        print("A empresa 1 tem o melhor preço!")
    else:
        print("A empresa 2 tem o melhor preço!")

else:
    k = (taxa_fixa_empresa_2 - taxa_fixa_empresa_1) / (taxa_variavel_empresa_1 - taxa_variavel_empresa_2)

    if k > 0:
        if taxa_variavel_empresa_1 < taxa_variavel_empresa_2:
            print(f"Empresa 1 é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a Empresa 2 é mais barata para distâncias maiores que {k:.2f} km.")
        else:
            print(f"Empresa 2 é mais barata para distâncias menores que {k:.2f} km, ambas têm o mesmo preço para {k:.2f} km e a Empresa 1 é mais barata para distâncias maiores que {k:.2f} km.")
    else:
        if taxa_fixa_empresa_1 < taxa_fixa_empresa_2:
            print("A Empresa 1 é sempre a melhor opção!")
        else:
            print("A Empresa 2 é sempre a melhor opção!")