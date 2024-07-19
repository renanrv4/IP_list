nome_ouvinte = input()
qtd_musicas = int(input())
menor_stream = 0
musica_mn = ''
maior_stream = 0
musica_mx = ''

# Repetição para receber os valores relacionados a música
for x in range(qtd_musicas):
    musica = input()
    qtd_streams = int(input())
    if qtd_streams > maior_stream:
      maior_stream = qtd_streams
      musica_mx = musica
      if menor_stream == 0:
        menor_stream = maior_stream
        musica_mn = musica
    elif qtd_streams < menor_stream:
      menor_stream = qtd_streams
      musica_mn = musica

if qtd_musicas == 0:
  print(f'{nome_ouvinte} é team Taylor e não ouviu Kanye West')
elif qtd_musicas == 1:
  print(f'A única música que {nome_ouvinte} ouviu foi {musica} com {qtd_streams} streams')
elif qtd_musicas > 1:
  if maior_stream == menor_stream:
    print(f'A música que {nome_ouvinte} mais ouviu foi {musica_mx} com {maior_stream} streams')
  else:
   print(f'A música que {nome_ouvinte} mais ouviu foi {musica_mx} com {maior_stream} streams')
   print(f'A música que {nome_ouvinte} menos ouviu foi {musica_mn} com {menor_stream} streams')