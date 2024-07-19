pontos_kayne = 0
outros_pontos = 0 

while True:
  n = input()
  if str(n) == 'FIM':
    break
  
  if int(n)%7 == 0 and int(n)%2 != 0:
    pontos_kayne += 20000000
  elif int(n)%2 == 0 and int(n)%7 != 0:
    pontos_kayne += 10000000
  elif int(n)%2 != 0 and int(n)%7 != 0:
    outros_pontos += 14000000
  
  if pontos_kayne + outros_pontos >= 300000000:
    break

if pontos_kayne > 170000000:
  print('O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.')
  print(f'Kanye conseguiu ao final da campanha um total de {pontos_kayne} votos.')
elif pontos_kayne < 130000000:
  print('Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.')
  print(f'Kanye conseguiu ao final da campanha um total de {pontos_kayne} votos.')
elif 130000000 < pontos_kayne < 170000000:
  print('A eleição está disputada, vamos ter um segundo turno!')
  print(f'Kanye conseguiu ao final da campanha um total de {pontos_kayne} votos.')
  pontos_kayne = 0
  while True:
    n = input()
    if str(n) == 'FIM':
      break
    
    if int(n)%7 == 0 and int(n)%2 != 0:
      pontos_kayne += 20000000
    elif int(n)%2 == 0 and int(n)%7 != 0:
      pontos_kayne += 10000000
    elif int(n)%2 != 0 and int(n)%7 != 0:
      outros_pontos += 14000000
    
    if pontos_kayne + outros_pontos >= 300000000:
      break

  if pontos_kayne > 170000000:
    print('Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.')
    print(f'Kanye conseguiu ao final da campanha um total de {pontos_kayne} votos.')
  else:
    print('Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.')
    print(f'Kanye conseguiu ao final da campanha um total de {pontos_kayne} votos.')

  
  
  