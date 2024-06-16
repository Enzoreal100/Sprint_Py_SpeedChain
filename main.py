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

def calculo_ntf(preco, posicao2):
    percentuais = [0.15, 0.12, 0.09, 0.06, 0.03, 0.0, -0.03, -0.06, -0.09, -0.12, -0.15]
    preco2 = []
    
    for i in range(len(posicao2)):
        pos = posicao2[i]
        valor = preco[i]
        if 1 <= pos <= 11:          
            valor = valor + (valor * percentuais[pos - 1])
        
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
    
    
def posicao(piloto, i, posicoes_usadas):#verifica a posicao que o usuario colocou em cada equipe para nao se repitir e ficar entre 1 e 11
    while True:
        position = input(f"Digite a posição do piloto {piloto[i]} \n --> ")
        if position.isnumeric():
            position = int(position)
            if 1 <= position <= 11:
                if position not in posicoes_usadas:
                    posicoes_usadas.append(position)
                    return position
                else:
                    print("Esta posição já foi usada. Por favor, digite uma posição diferente.")
            else:
                print("Digite um valor entre 1 e 11.")
        else:
            print("Entrada inválida. Digite um número.")

#Construção do código
opcoes_sair = ["1","2","3"]
#posicao_nova = []
piloto = ["Equipe1","Equipe2","Equipe3","Equipe4","Equipe5","Equipe6","Equipe7","Equipe8","Equipe9","Equipe10","Equipe11",]
posiçao = []
posicoes_usadas = []
valor = [10,20,30,40,50,100,12,15,22,77,88]


while True:
    print("Bem-vindo!")
    escolha = forca_escolha(opcoes_sair, "Digite [1] para ver os preços de nft de cada Equipe \n [2] Para colocar a posição de cada Equipe na mais nova corrida \n [3] Para sair\n -->")
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
            position = int(posicao(piloto, i, posicoes_usadas))
            posiçao.append(position)
            print(f"Posição do {piloto[i]}: {position}")       
       
        novos_valores = calculo_ntf(valor, posiçao)
        
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
    
            
            
            

