orcamento_total = float(input("Digite o valor total em reaisi para a festa do Rodri: "))
numero_convidados = int(input("Digite a quantidade de convidados que estarão presentes na festa: "))
local_festa = input("Local onde a festa será realizada: ").lower()
cantor_convidado = input("Digite o cantor contratado para a festa: ").lower()
cotacao_euro = float(input("Digite a cotação do euro: "))
orcamento_euro = orcamento_total / cotacao_euro
gasto_convidado = orcamento_euro / numero_convidados

if(orcamento_euro < 1000000):
    print(f"Acabei de receber a informação que o orçamento total da festa será {orcamento_total} de euros. Poxa, com um orçamento desses vai ser difícil fazer a festa bombar! Vou divulgar essa informação pros sites de fofocas pra flopar a festa")

else:
    print("Poxa, esse cara tá podendo! Vai ser um festão, mas eu vou encontrar alguma coisa para que flope.")

if(gasto_convidado >= 5000):
    print("Eita, cancela o repasse da informação pros sites de fofocas! Gastando isso tudo por pessoa, vai continuar sendo um luxo.")

else:
    print("Que vergonha, viu? O povo vai passar fome. Divulgue isso agora!")

if(local_festa == "hotel pera palace" or "hotel copacabana palace"):
    print("Eu conheço os donos e são meus amigos! Vou pedir pra recusarem a oferta!")

else:
    print("Poxa, não vou conseguir fazer nada!")

if(cantor_convidado == "anitta" or "thiaguinho"):
    print(f"Duvido que aceite, Rodri fez isso pra me estressar! Claro que {cantor_convidado} não vai fazer isso comigo!")

else:
    print("Vou fazer uma oferta maior! Isso precisa flopar!")