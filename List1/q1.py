piloto = str(input())
distancia = float(input())
tempoh = float(input())

vlcmed = distancia/tempoh

if vlcmed > 227:
  print(f'{piloto} se deu muito bem na prova de hoje!!')
elif vlcmed == 227:
  print(f'{piloto} teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!' )
else:
  print(f'{piloto} não se deu tão bem. É preciso melhorar isso!')