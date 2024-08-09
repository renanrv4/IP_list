def cifra_cesar(musica_cod, cifra):
    resultado = ''
    for letra in musica_cod:
        if not letra.isalpha():
            resultado += letra
        else:
            if letra.isupper():
                letra = letra.lower()
                char_index = cifra.index(letra)
                resultado += cifra[char_index-3].upper()
            else:
                char_ind = cifra.index(letra)
                resultado += cifra[char_ind-3]
    return resultado

def checagem_da_musica(nome_musica, albuns):
    for album in albuns.keys():
        for musica in albuns[album].keys():
            if nome_musica == musica:
                return album
    return ''

def album_maior_pontuacao(_albuns):
    album, album_vencedor = {}, {}
    for n_album in _albuns.keys():
        album[n_album] = 0
        for points in _albuns[n_album].values():
            album[n_album] += points
    for pontos in album.keys():
        maior = True
        for pontos_comp in album.values():
            if album[pontos] < pontos_comp:
                maior = False
        if maior:
            album_vencedor[pontos] = album[pontos]
            return album_vencedor
        
def musica_maior_pontuacao(_albuns_dict, album_vencedor):
    musica_vencedora = {}
    for alb in album_vencedor.keys():
        for item_musica in _albuns_dict[alb].keys():
            maior_pontuacao = True
            for item_musica_comp in _albuns_dict[alb].keys():
                if _albuns_dict[alb][item_musica] < _albuns_dict[alb][item_musica_comp]:
                    maior_pontuacao = False
            if maior_pontuacao:
                musica_vencedora[item_musica] = _albuns_dict[alb][item_musica] 
                return musica_vencedora
            
albuns_dict = {
    "sweetener": {"no tears left to cry": 0, "the light is coming": 0, "better off": 0, "everytime": 0},
    "thank u, next": {"NASA": 0, "thank u, next": 0, "break up with your girlfriend, i'm bored": 0, "bad idea": 0},
    "Positions": {"motive": 0, "safety net": 0, "nasty": 0, "pov": 0},
    "eternal sunshine": {"yes, and?": 0, "eternal sunshine": 0, "the boy is mine": 0, "we can't be friends": 0} 
}

alfabeto_cifrado = 'defghijklmnopqrstuvwxyzabc'
limite = int(input())

condicao = True
while condicao:
    musicas_info = input().split(' - ')
    if musicas_info[0] == 'FIM':
        condicao = False
    else:
        nome_decifrado, pontos_yeah = cifra_cesar(musicas_info[0], alfabeto_cifrado), int(musicas_info[1])
        print(f'O nome da música decifrada é: {nome_decifrado}')
        music_in_dict = checagem_da_musica(nome_decifrado, albuns_dict)

        if music_in_dict == '':
            print('Poxa, essa música não está na discografia da base do nosso estúdio!')
        else:
            albuns_dict[music_in_dict][nome_decifrado] += pontos_yeah
            print(f'Ótimo! A música está na discografia da nossa base de dados!')
            print(f'O album da música decifrada é {music_in_dict}')
            if pontos_yeah <= 5:
                print('A diva do pop não se empolgou nessa e decepcionou os arianators.')
            elif 5 < pontos_yeah < 10:
                print('Ariana fez o dever de casa e entregou uma música na média para os seus fãs.') 
            elif pontos_yeah >= 10:
                print('AVISA QUE ESSA JÁ É HIT NOS CHARTS!')

        album_pontuacao = album_maior_pontuacao(albuns_dict)
        for pontos in album_pontuacao.values():
            if pontos >= limite:
                print(f'Atenção! O limite de pontuação foi atingido pelo álbum {music_in_dict}!')
                condicao = False

print('Fim da análise!\n')
musica_pontuacao = musica_maior_pontuacao(albuns_dict, album_pontuacao)
for album_info in album_pontuacao.items():
    print(f'O álbum da estrela Ariana Grande com a maior pontuação foi {album_info[0]}, com um total de {album_info[1]} pontos!')
for musica_info in musica_pontuacao.items():
    print(f'Entre todas as faixas desse álbum, a melhor pontuada foi {musica_info[0]}, que obteve {musica_info[1]} pontos')