vmax = int(input())
tempo = input()

if 286 <= vmax <= 310 and tempo != 'neblina':
  print('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')
elif 261 <= vmax <= 285 and tempo == 'neblina':
    print('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')
elif 261 <= vmax <= 285 and tempo != 'neblina':
  print('Senna corria em Ímola, onde infelizmente fez sua última corrida.')
elif 250<= vmax <= 260 and tempo == 'neblina':
  print('Senna corria em Ímola, onde infelizmente fez sua última corrida.')
else:
  print('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')
