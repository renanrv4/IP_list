pcharles = int(input())
pmax = int(input())

if pcharles == 0:
  print('Oxe! E vai morrer por causa de 25 pontos?')
elif pcharles == 25:
  print('O meu favorito venceu! Pode torar o aco Verstappen')
elif 15 <= pcharles < 25:
  print('Esse Charles eh arretado mesmo')
elif 10 <= pcharles <= 12:
  print('Ele eh desenrolado demais')

if pcharles > 0 and abs(pcharles - pmax) <= 4:
  print('Ta com a molestia, vai perder para Max Verstappen eh')
elif (pcharles - pmax) > 4:
  print('Deu o sangue')