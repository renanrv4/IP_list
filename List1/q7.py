pilotoA = input()
tempoA = float(input())
pilotoB = input()
tempoB= float(input())
pilotoC = input()
tempoC = float(input())

print('E o Pódio do GP de Mônaco é:')

if tempoA < tempoB and tempoA < tempoC:
  print(f'{pilotoA} está no lugar mais alto do pódio com tempo de {tempoA} horas de corrida.')
  if(tempoB < tempoC):
    print(f'{pilotoB} está no segundo lugar do pódio com tempo de {tempoB} horas de corrida.')
    print(f'{pilotoC} está no terceiro lugar do pódio com tempo de {tempoC} horas de corrida.')
  else:
    print(f'{pilotoC} está no segundo lugar do pódio com tempo de {tempoC} horas de corrida.')
    print(f'{pilotoB} está no terceiro lugar do pódio com tempo de {tempoB} horas de corrida.')
  print(f'Galvão, temos um momento histórico da Fórmula 1, {pilotoA} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempoA} horas de prova.')

elif tempoB < tempoA and tempoB < tempoC:
  print(f'{pilotoB} está no lugar mais alto do pódio com tempo de {tempoB} horas de corrida.')
  if(tempoA < tempoC):
    print(f'{pilotoA} está no segundo lugar do pódio com tempo de {tempoA} horas de corrida.')
    print(f'{pilotoC} está no terceiro lugar do pódio com tempo de {tempoC} horas de corrida.')
  else:
    print(f'{pilotoC} está no segundo lugar do pódio com tempo de {tempoC} horas de corrida.')
    print(f'{pilotoA} está no terceiro lugar do pódio com tempo de {tempoA} horas de corrida.')
  print(f'Galvão, temos um momento histórico da Fórmula 1, {pilotoB} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempoB} horas de prova.')

else:
  print(f'{pilotoC} está no lugar mais alto do pódio com tempo de {tempoC} horas de corrida.')
  if(tempoB < tempoA):
    print(f'{pilotoB} está no segundo lugar do pódio com tempo de {tempoB} horas de corrida.')
    print(f'{pilotoA} está no terceiro lugar do pódio com tempo de {tempoA} horas de corrida.')
  else:
    print(f'{pilotoA} está no segundo lugar do pódio com tempo de {tempoA} horas de corrida.')
    print(f'{pilotoB} está no terceiro lugar do pódio com tempo de {tempoB} horas de corrida.')
  print(f'Galvão, temos um momento histórico da Fórmula 1, {pilotoC} acaba de fazer história no GP de Mônaco ao terminar a corrida com {tempoC} horas de prova.')

