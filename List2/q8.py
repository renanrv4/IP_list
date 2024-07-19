candidato_1 = input()
candidato_2 = input()

delegados_c1 = 0
delegados_c2 = 0
votot_c1 = 0
votot_c2 = 0

if candidato_1 != 'Kanye West' and candidato_2 != 'Kanye West':
    print('Sem o Ye, sem eleição!')
else:
    while True:
        est_del = input()
        if est_del == 'FIM':
            break
        estado = est_del.split(',')
        voto_c1 = input()
        if voto_c1 != 'Taylor Swift roubou as urnas!':
            voto_c2 = input()
        while voto_c1 == 'Taylor Swift roubou as urnas!' or  voto_c2 == 'Taylor Swift roubou as urnas!':
            print('A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!')
            voto_c1 = input()
            if voto_c1 != 'Taylor Swift roubou as urnas!':
               voto_c2 = input()
        voto_total = int(voto_c1) + int(voto_c2)
        if int(voto_c1) > int(voto_c2):
            print(f'{candidato_1} obteve maioria no(a) {estado[0]} com {int((int(voto_c1)/voto_total)*100)}% dos votos.')
            delegados_c1 += int(estado[1])
            votot_c1 += int(voto_c1)
        else:
            print(f'{candidato_2} obteve maioria no(a) {estado[0]} com {int((int(voto_c2)/voto_total)*100)}% dos votos.')
            delegados_c2 += int(estado[1])
            votot_c2 += int(voto_c2)

    if delegados_c1 > delegados_c2:
        print(f'Temos o resultado final! {candidato_1} vence a disputa pela presidência, com o apoio de {delegados_c1} delegados do colégio eleitoral e {votot_c1} votos populares.')
        if candidato_1 == 'Kanye West':
            print('\"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know.\"')
        else:
            print('\"Não tem problema, eu obtive o molho!\"')
    else:
        print(f'Temos o resultado final! {candidato_2} vence a disputa pela presidência, com o apoio de {delegados_c2} delegados do colégio eleitoral e {votot_c2} votos populares.')
        if candidato_2 == 'Kanye West':
            print('\"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know.\"')
        else:
            print('\"Não tem problema, eu obtive o molho!\"')
    
  
