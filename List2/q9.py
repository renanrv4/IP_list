n_musicas = int(input())
print('Bem vindo ao jogo da forca do ye!')
pontos = 0

for x in range(n_musicas):
  musica = input()
  musica_forca = ''
  for l in musica:
    if l == ' ':
        musica_forca += ' '
    else:
        musica_forca += '_'
  if x < (n_musicas-1):
    print(f'Esta é a música {x+1} de {n_musicas}.')
  else:
    print('Última música!')

  # Tentativas
  j = 0
  while j < (len(musica)*2) and musica_forca != musica:
    chute = input()
    if chute in musica:
        if chute in musica_forca:
          print('Já tinha colocado essa letra antes, preciso de mais atenção.')
        for m in range(len(musica)):
           if musica[m] == chute:
              if chute in musica and chute not in musica_forca:
                print('Uhuuuuu! Consegui adivinhar uma letra!')
              musica_forca = musica_forca[:m] + chute + musica_forca[m+1:]
    elif chute not in musica:
        print(f'Eita! Parece que a letra {chute} não está na música secreta!')
    print(f'Resposta atual: {musica_forca}')

    j += 1

  if musica_forca == musica:
    print('Isso! Consegui acertar uma música!')
    pontos += 1
  else:
    print(f'Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!')
    musica_forca = musica

print(f'Consegui acertar {pontos} músicas de {n_musicas}!')

# Porcentagem de acertos
porcentagem = (pontos/n_musicas)*100

if porcentagem <= 50:
   print('Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!')
elif 50 < porcentagem <= 75:
   print('Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.')
elif 75 < porcentagem < 100:
   print('Estou quase chegando na perfeição! Só não consegui porque não gosto de todos os álbuns.')
else:
   print('Eu sou o próprio Kanye West.')
    

