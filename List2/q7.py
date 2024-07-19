qtd_alunos = int(input())
taylor = 0
beyonce = 0

# Primeira votação
for x in range(qtd_alunos):
  voto = input()
  if voto == 'taylor swift':
    taylor += 1
    print(f'Aluno {x+1} votou na Taylor Swift.')
  else:
    beyonce += 1
    print(f'Aluno {x+1} votou na Beyoncé.')

print('Contagem de votos:')
print(f'Taylor Swift: {taylor} votos')
print(f'Beyoncé: {beyonce} votos')

# Nova contagem
if taylor == beyonce:
  print('Empate! Iniciando rodada de debate.')
  print('Alunos, agora é a sua chance de convencer os outros a mudar de voto!')
  for x in range(qtd_alunos):
    decisao = input()
    if decisao == 'sim':
      novo_voto = input()
      if novo_voto == 'taylor swift':
        taylor += 1
        print(f'Aluno {x+1} mudou seu voto para Taylor Swift.')
      else:
        beyonce += 1
        print(f'Aluno {x+1} mudou seu voto para Beyoncé.')
    else:
      print(f'Aluno {x+1} não mudou seu voto.')
  print('Nova contagem de votos após o debate:')
  print(f'Taylor Swift: {taylor} votos')
  print(f'Beyoncé: {beyonce} votos')

# Ganhadora na primeira ou na nova contagem
if taylor > beyonce:
  print(f'Taylor Swift venceu com {taylor} votos! Kanye West tá irritado com isso.')
elif beyonce > taylor:
  print(f'Beyoncé venceu com {beyonce} votos! Será que Kanye West estava certo?')

# Voto decisivo
if taylor == beyonce:
  print('Aldo, como presidente do evento, tem o voto decisivo.')
  voto_decisivo = input()
  if voto_decisivo == 'taylor swift':
    taylor += 1
    print('Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.')
  else:
    beyonce += 1
    print('Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?')
    
