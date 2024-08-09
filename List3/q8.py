# Salas disponíveis
salas = ['artesanato', 'copa', 'caldeira', 'aquário', 'mural']

# Conjuntos copa
recursos_primavera = ["raiz-forte", "narciso", "alho-poro", "dente-de-leao"]
recursos_verao = ["uva", "cafe-de-jardim", "ervilha-de-cheiro"]
recursos_outono = ["amora", "cogumelo-comum", "avela", "ameixa-selvagem"]
recursos_inverno = ["raiz-de-inverno", "fruta-de-cristal", "inhame-de-neve", "flor-de-acafrao"]

copa = ['recursos da primavera', 'recursos do verao', 'recursos do outono', 'recursos do inverno']
copa_conj = [recursos_primavera, recursos_verao, recursos_outono, recursos_inverno]

# Conjuntos artesanato
plantacoes_primavera = ["chirivia", "vagem", "couve-flor", "batata"]
plantacoes_verao = ["tomate", "mirtilo", "melao", "pimenta-quente"]
plantacoes_outono =  ["milho", "beringela", "abobora", "inhame"]
artesao = ["mel", "geleia", "queijo", "tecido"]

artesanato = ['plantacoes da primavera', 'plantacoes do verao', 'plantacoes do outono', 'artesao']
artesanato_conj = [plantacoes_primavera, plantacoes_verao, plantacoes_outono, artesao]

# Inputs das salas, conjuntos e itens
sala = input()
conjuntos = input().split(', ')
itens = input().split(', ')

# Listas para caso haja itens e/ou conjuntos repetidos
item = []
conjuntos_rep = []
repetidos = 0

# Lista dos itens em todos os conjuntos
itens_list = []

# Checagem das salas escolhidas
if sala not in salas:
    print('Essa sala não está no centro comunitário') 
elif sala != salas[0] and sala != salas[1]:
    print(f'Eu já conclui {sala}, não precisa doar mais itens para essa sala')

if conjuntos[0] == ' ' or itens[0] == ' ':
    print('Sérgio esqueceu algumas informações, será que ele pode enviar novamente?')
else:
    if sala == 'copa':
        # Loops para identificar se o conjunto realmente pertence a sala
        for conj in conjuntos:
            if conj not in conjuntos_rep:
                conjuntos_rep.append(conj)
                for c in copa:
                    if conj == c:
                        copa_index = copa.index(c)
                        for el in copa_conj[copa_index]:
                            itens_list.append(el)
            else:
                repetidos += 1
        # Comparando os itens digitados com os itens de cada conjunto
        for i in itens:
            if i in itens_list and i not in item:
                print(f'{i} vai ser entregue ao centro logo!')
                item.append(i)
            elif i in itens_list and i in item:
                repetidos += 1
            elif i not in item:
                print(f'{i} pode ser analisado depois')
        
        if repetidos >= 1:
            print('Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')

    elif sala == 'artesanato':
        # Loops para identificar se o conjunto realmente pertence a sala
        for conj in conjuntos:
            if conj not in conjuntos_rep:
                conjuntos_rep.append(conj)
                for a in artesanato:
                    if conj == a:
                        artesanato_index = artesanato.index(a)
                        for el in artesanato_conj[artesanato_index]:
                            itens_list.append(el)
            else:
                repetidos +=1
        # Comparando os itens digitados com os itens de cada conjunto
        for i in itens:
            if i in itens_list and i not in item:
                print(f'{i} vai ser entregue ao centro logo!')
                item.append(i)
            elif i in itens_list and i in item:
                repetidos += 1
            elif i not in item:
                print(f'{i} pode ser analisado depois')
        
        if repetidos >= 1:
            print('Acho que Sérgio se enganou e enviou duas vezes a mesma coisa, mesmo assim vamos continuar a receber…')
        