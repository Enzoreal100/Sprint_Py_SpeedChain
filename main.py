# valores simulando DB


# funções
def meu_index (lista,elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
            return i
    

def maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] >= maior:
            maior = lista[i]
    return maior


def menor (lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] <= menor:
            menor = lista[i]
    return menor

def calculo_ntf(preco,posicao):
    preco2 = []
    for i in posicao:
        match i:
            case 1:
                valor = preco[meu_index(posicao,1)]
                valor = valor + (valor * .15)
                #print(valor)
                preco2.append(valor)
                #preco2[] = valor
            case 2:
                valor = preco[meu_index(posicao,2)]
                valor = valor + (valor * .12)
            # print(valor)
                preco2.append(valor)
            # preco[] = valor
            case 3:
                valor = preco[meu_index(posicao,3)]
                valor = valor + (valor * .09)
                preco[meu_index(posicao,3)] = valor
                #print(valor)
                preco2.append(valor)
            case 4:
                valor = preco[meu_index(posicao,4)]
                valor = valor + (valor * .06)
                preco[meu_index(posicao,4)] = valor
                #print(valor)
                preco2.append(valor)
            case 5:
                valor = preco[meu_index(posicao,5)]
                valor = valor + (valor * .03)
                preco[meu_index(posicao,5)] = valor
            # print(valor)
                preco2.append(valor)
            case 6:
                valor = preco[meu_index(posicao,6)]
                #print(valor)
                preco2.append(valor)
    return preco2

def forca_escolha(lista,msg):
    while True:
        escolha = input(msg)
        if escolha in lista:
            return escolha
        else:
            print("---------------------")
            print("Escolha uma opção válida!")
            print("Opções disponíveis: ", lista)
            
def sair_continuar():
    sair_continuar = ["sair","continuar"]
    sair = forca_escolha(sair_continuar, "Digite [sair] para e [continuar] para voltar ao menu \n -->")
    if sair == "continuar":
        return True
    elif sair == "sair":
        return False
    
    
def posicao(piloto, i):
    while True:
        position = input(f"Digite a posição do piloto {piloto[i]} \n -->")
        if position.isnumeric():
            position = int(position)
            if 1 <= position <= 6:
                return position
            else:
                print("Digite um valor entre 1 e 6")
        else:
            print("Entrada inválida. Digite um número.")
            

#Construção do código
opcoes_sair = ["1","2","3"]
posicao_nova = []
piloto = ["Piloto1","Piloto2","Piloto3","Piloto4","Piloto5","Piloto6",]
posiçao = [5,4,3,1,2,6]
valor = [10,20,30,40,50,100]

print("Bem-vindo!")
while True:
    escolha = forca_escolha(opcoes_sair, "Digite: \n [1] para ver os preços de nft de cada piloto \n [2] Para colocar a posição de cada piloto na mais nova corrida \n [3] Para sair\n -->")
    if escolha == "1":
        for i in range(len(piloto)):
            print(f"O valor do piloto {piloto[i]} é de R${valor[i]}")
        sair = sair_continuar()
        if sair:
            continue
        else:
            break
    if escolha == "2":
        for i in range(len(piloto)):
            position = posicao(piloto, i)
            posicao_nova.append(position)
            print(f"Posição do {piloto[i]}: {position}")       
       
        novos_valores = calculo_ntf(valor, posicao_nova)
        
        for i in range(len(piloto)):
            print(f"Piloto: {piloto[i]}")
            print(f"  Valor Antigo: R${valor[i]}")
            print(f"  Novo Valor: R${novos_valores[i]}")   
            
        
        sair = sair_continuar()
        if sair:
            continue
        else:
            break
    if escolha == "3":
        print("Saindo...")
        break
    
            
            
            

