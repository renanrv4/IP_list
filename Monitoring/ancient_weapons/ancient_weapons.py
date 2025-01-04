def calcular_pb(itens, habilidades, faccao, posicao):
    pb = 0  # Poder de Batalha inicial

    # Armas Especiais e mensagens de facção
    armas_especiais = {
        "Arco de Catende": ("Catende será vitoriosa, Joab nos levará a glória!!!", "Good"),
        "Cajado da Morte do Ibura": ("Esse cajado possui a energia da morte consigo, melhor prendê-la no mundo dos espelhos.", "Evil"),
        "Espada do Sol do Piauí": ("Essa espada é abençoada pelo Sol, essa espada pertenceu ao guerreiro Luis, devemos usá-la para derrotar as forças do mal.", "Good"),
        "Arco do Tupã": ("Essa arma é abençoada pela aldeia do trovão, comandada por Júlia, uma arma sagrada podemos usá-la para derrotar o exército de Lavoisier.", "Good"),
        "Livro das Canções": ("Esse livro possui todos os cânticos da terra longínqua de Tabira, o livro foi escrito pelo bardo Renan, com eles podemos tornar o nosso exército mais poderoso.", "None"),
        "Tridente das Águas de Aracaju": ("Essa arma pertenceu ao general dos Mares, Renato, ele foi responsável pela derrota de muitos povos. Precisamos nos livrar dessa arma.", "Evil"),
        "Manoplas Elementais da terra e água": ("Essa arma possui a alma de vários povos antigos, o possuidor dessa arma quebrou diversos tabus. Valter foi o dono dela, ele possui vidas inocentes em suas mãos.", "Evil")
    }
    mensagens = []
    itens_especiasi = 0
    # 1. Bônus de Itens
    for item in itens:
        pb += item["bonus"]
        
        # Checar se o item é uma arma especial
        if item["nome"] in armas_especiais:
            # Checar se o jogador está na facção correta para o bônus especial
            if (faccao == armas_especiais[item["nome"]][1] or item["nome"] == "Livro das Canções"):
                itens_especiasi += 1
            if (armas_especiais[item["nome"]][1] == "Good" or faccao == "Good"):
                mensagens.append(armas_especiais[item["nome"]][0])
            else:
                # Mensagem alternativa para facções diferentes
                if item["nome"] == "Arco de Catende":
                    mensagens.append("Esse arco foi utilizado pelos guerreiros de Catende, melhor jogar essa arma nas profundezas.")
                elif item["nome"] == "Cajado da Morte do Ibura":
                    mensagens.append("As sombras vão dominar Recife, Lavoisier trará a escuridão!!!")
                elif item["nome"] == "Espada do Sol do Piauí":
                    mensagens.append("Essa espada possui o poder das chamas divinas, devemos prender essa arma na fenda dimensional.")
                elif item["nome"] == "Arco do Tupã":
                    mensagens.append("O arco de tupã é uma arma sagrada, devemos selá-lo na tumba dos campeões.")
                elif item["nome"] == "Tridente das Águas de Aracaju":
                    mensagens.append("Com essa arma podemos ter o mar como aliado, devemos usar essa arma para dominar as águas de Recife e suas feras (os tubarões).")
                elif item["nome"] == "Manoplas Elementais da terra e água":
                    mensagens.append("As manoplas de Valter são ótimas para causar catástrofes naturais, devemos usá-las para atormentar vilas inimigas.")
                elif item["nome"] == "Livro das Canções":
                    mensagens.append(armas_especiais[item["nome"]][0])

    # 2. Bônus de Habilidades para Armas
    for item in itens:
        if item["tipo"] == "arma":
            tipo_ataque = item.get("tipo_ataque")
            if tipo_ataque == "corpo a corpo":
                pb += habilidades.get("força", 0) * 5
                pb += habilidades.get("agilidade", 0) * 3
            elif tipo_ataque == "à distância":
                pb += habilidades.get("agilidade", 0) * 3
            elif tipo_ataque == "mágico":
                pb += habilidades.get("inteligência", 0) * 5

    # 3. Bônus de Conjunto
    tipos_itens = set([item["tipo"] for item in itens])
    if "arma" in tipos_itens and "armadura" in tipos_itens:
        pb += 15
        if "acessorio" in tipos_itens:
            pb += 20

    # 4. Penalidade de Peso
    if len(itens) > 4:
        excesso = len(itens) - 4
        pb *= (0.95 - (excesso-1)/20)
    # 5. Posição dentro da Facção
    if posicao == "soldado":
        pb += 10
    elif posicao == "general":
        pb *= 1.05
    # 6. Buffs especiais
    pb *= (1 + itens_especiasi/10)
    # Print mensagens das armas especiais
    for mensagem in mensagens:
        print(mensagem)

    # Retorno final do PB
    return f"Pontos de Batalha: {round(pb)}"


itens, habilidades = [], {}
faccao, posicao, valores = "", "", ""

print("Bem vindo ao mundo de AQW!!")

while valores != "FIM DA LISTA":
    valores = input()
    valores_split = valores.split(" | ")
    if valores != "FIM DA LISTA":
        if valores_split[1] == "arma":
            tipo_ataque = input()
            itens.append({
                "nome": valores_split[0], 
                "tipo": valores_split[1],
                "bonus": int(valores_split[2]),
                "tipo_ataque": tipo_ataque})
        else:
            itens.append({"nome": valores_split[0], 
                "tipo": valores_split[1],
                "bonus": int(valores_split[2]),})
            
habilidades_atributos = input().split(" | ")

for h in range(len(habilidades_atributos)):
    habilidades_atributos[h] = int(habilidades_atributos[h])
habilidades = {"força":habilidades_atributos[0], "agilidade": habilidades_atributos[1], "inteligência":habilidades_atributos[2]}
sua_faccao = input().split(" | ")
faccao, posicao = sua_faccao[0], sua_faccao[1]
resultado = calcular_pb(itens, habilidades, faccao, posicao)
print(resultado)