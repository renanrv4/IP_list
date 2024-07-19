rodadas = int(input())
pontuacao_k = 0
pontuacao_t = 0
descontentamento_k = 0
descontentamento_t = 0
rodadasvenc_k = 0
rodadasvenc_t = 0
rodadaspassadas = 0

while rodadaspassadas < rodadas and descontentamento_k < 5 and descontentamento_t < 5 and rodadasvenc_k < 3 and rodadasvenc_t < 3:
  print(f'{rodadaspassadas+1}° RODADA:')
  
  # Avaliação do kanye
  musica_kayne = input()
  j = 0
  while j < 3:
    aval_k = input()
    if aval_k == 'boa':
      pontuacao_k += 2
    elif aval_k == 'média':
      pontuacao_k += 1
    elif aval_k == 'ruim':
      pontuacao_k -= 3
    elif aval_k == 'péssima':
      b = True
      while b:
        descontentamento = input()
        if descontentamento == 'ORDEM':
          b = False
        else:
          descontentamento_k += 1
    j+=1
  # Avaliação da taylor
  if descontentamento_k < 5:
    musica_taylor = input()
    t = 0
    while t < 3:
      aval_t = input()
      if aval_t == 'boa':
        pontuacao_t += 2
      elif aval_t == 'média':
        pontuacao_t += 1
      elif aval_t == 'ruim':
        pontuacao_t -= 3
      elif aval_t == 'péssima':
        a = True
        while a:
          descontentamento = input()
          if descontentamento == 'ORDEM':
            a = False
          else:
            descontentamento_t += 1
      t += 1
  if descontentamento_k < 5 and descontentamento_t < 5:
    if pontuacao_t > pontuacao_k:
        print(f'O(a) vencedor(a) da {rodadaspassadas+1}° rodada foi Taylor Swift')
        rodadasvenc_t += 1
    elif pontuacao_k > pontuacao_t:
        print(f'O(a) vencedor(a) da {rodadaspassadas+1}° rodada foi Kanye West')
        rodadasvenc_k += 1
    elif pontuacao_t == pontuacao_k:
        print(f'Não houve vencedor na {rodadaspassadas+1}° rodada')
  pontuacao_k = 0
  pontuacao_t = 0
  rodadaspassadas += 1

if descontentamento_t >= 5: 
  print('Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!')
  print('O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!')
elif descontentamento_k >= 5:
  print('Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!')
  print('O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!')
elif rodadasvenc_t >= 3 or rodadasvenc_t > rodadasvenc_k:
  print(f'O(a) vencedor(a) do Cin Awards, com um total de {rodadasvenc_t} vitórias, é Taylor Swift, parabéns!')
elif rodadasvenc_k >= 3 or rodadasvenc_k > rodadasvenc_t:
  print(f'O(a) vencedor(a) do Cin Awards, com um total de {rodadasvenc_k} vitórias, é Kanye West, parabéns!')
elif rodadasvenc_k == rodadasvenc_t:
  print('Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!')
  