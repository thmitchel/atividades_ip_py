taxa_fixa_empresa_1 = float(input("Digite a taxa fixa da empresa 1: "))
taxa_variavel_empresa_1 = float(input("Digite a taxa variável da empresa 1: "))

taxa_fixa_empresa_2 = float(input("Digite a taxa fixa da empresa 2: "))
taxa_variavel_empresa_2 = float(input("Digite a taxa variável da empresa 2: "))

k = float(input("Digite a distancia em quilometros: "))
P1 = (taxa_variavel_empresa_1 * k) + taxa_fixa_empresa_1
P2 = (taxa_variavel_empresa_2 * k) + taxa_fixa_empresa_2
