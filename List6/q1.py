def adicionar_album (album_list: list, album, artista, ano, gen):
    album_list.append((album, artista, ano, gen))
    return True

def consultar_genero (albuns_list, genero_consulta):
    qtd_album = 0
    albuns_consulta = []
    for album in albuns_list:
        if album[-1] == genero_consulta:
            qtd_album += 1
            albuns_consulta.append(album)
    return qtd_album, albuns_consulta

albuns = [('Abbey Road', 'The Beatles', 1969, 'Rock'),
('The Dark Side of the Moon', 'Pink Floyd', 1973, 'Rock'),
('Riot!', 'Paramore', 2007, 'Rock'),
('Fearless', 'Taylor Swift', 2008, 'Pop'),
('Da Lama ao Caos', 'Chico Science e Nação Zumbi', 1994, 'Manguebeat'),
('Gal Costa', 'Gal Costa', 1969, 'MPB'),
('Sim', 'Vanessa da Mata', 2007, 'MPB'),
('As 20 Melhores', 'Luiz Gonzaga', 2004, 'Forró'),
('O Melhor de Dominguinhos', 'Dominguinhos', 2013, 'Forró'),
('Alucinação', 'Belchior', 1976, 'MPB'),
('Samba Esquema Novo', 'Jorge Ben Jor', 1963, 'Samba')]

genero_catalogo = ['Rock', 'Pop', 'Manguebeat', 'MPB', 'Forró', 'Samba']

condicao = True
nome_album = ''
while condicao:
    acao = input()

    if acao != 'CONSULTAR' and acao != 'FIM':
        nome_album = acao
        nome_artista = input()
        ano_lancamento = input()
        genero = input() 
        adicionar_album(albuns, nome_album, nome_artista, ano_lancamento, genero)
        print('Este foi o novo álbum adicionado:')
        print(f'- {nome_album} do/da artista/banda {nome_artista} lançado em {ano_lancamento}')
        if genero not in genero_catalogo:
            genero_catalogo.append(genero)
            print('Oba, você adicionou um novo estilo musical ao catálogo!')
    else:
        if acao == 'CONSULTAR':
            genero_music = input()
            consulta = consultar_genero(albuns, genero_music)
            if consulta[0] > 0:
                print(f'Nessa galeria há {consulta[0]} albuns de {genero_music}. Os albuns encontrados foram:')
                for album_consulta in consulta[1]:
                    print(f'- {album_consulta[0]} do/da artista/banda {album_consulta[1]} lançado em {album_consulta[2]}')
            else:
                print('Você vai precisar adicionar um novo álbum ao catálogo! Não encontramos nenhum álbum desse estilo musical!')
        elif acao == 'FIM': 
            condicao = False
