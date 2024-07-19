condicoes_clima = input()
if condicoes_clima == 'chuvoso':
  pista_molhada = input()
temperatura = input()
desempenho = input()
posicao = int(input())

# clima: ensolarado, nublado e chuvoso.
# temperatura: alta, moderada e baixa.
# desempenho: bom ou ruim
# posicao: entre 20

print('Estratégia de prova de Max Verstappen!')

# clima e temperatura 
if condicoes_clima == 'ensolarado' and temperatura == 'alta':
  print('Está fazendo muito calor, opte por pneus de compostos mais duros para que eles durem mais!')
elif condicoes_clima == 'ensolarado' and temperatura != 'alta':
  print('Max, está sol, mas devido ao clima frio, hoje é melhor usar pneus mais macios.')
# clima nublado
elif condicoes_clima == 'nublado' and temperatura == 'alta':
  print('Devido ao calor vamos iniciar a corrida com pneus mais duros, mas fique alerta para uma mudança repentina de clima!')
elif condicoes_clima == 'nublado' and temperatura != 'alta':
  print('Max, para enfrentar o clima e a temperatura de hoje o ideal será usar pneus médios!')
# clima chuvoso
elif condicoes_clima == 'chuvoso' and pista_molhada == 'True':
  print('Cuidado! Está chovendo e a pista está escorregadia, considere usar pneus de chuva e reduza a velocidade nas curvas.')
else:
  print('Está chovendo, mas a pista ainda está seca. Considere usar pneus de chuva ou colocá-los durante a corrida. Atenção nas curvas!')

# desempenho e posicao
if posicao == 1 and desempenho == 'bom':
  print('Max, você vai largar na frente e teve um desempenho muito bom nos treinamentos. Pode optar por uma estratégia mais conservadora e com menos paradas nos boxes.')
elif posicao == 1 and desempenho == 'ruim':
  print('Max, você vai largar em primeiro, mas mantenha a atenção, seu desempenho no treino não foi tão bom.')
elif posicao <= 12:
  print('Não estamos largando atrás, mas precisamos do seu talento Max! É hora de quebrar alguns recordes, opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
else:
  print('Estamos largando atrás e precisamos correr tirar a diferença. Opte por uma estratégia mais agressiva e com mais paradas nos boxes.')
  
