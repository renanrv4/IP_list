qtd_exercicios = int(input())

i = True
eficacia = 0

while i == True:
  tipo_treino = input()
  if tipo_treino == 'Fim do Treino':
    i = False
  else:
    print(tipo_treino)
    for x in range(qtd_exercicios):
      nome_musica = input()
      nota_musica = int(input())
      print(f'{x+1}° música {nome_musica} tocando agora')
      if nota_musica >= 7:
        print('O padre Marcelo está inspirado, conseguiu finalizar suas séries!')
        eficacia += 1
      elif nota_musica < 7:
        print('O padre Marcelo está desanimado, não conseguiu finalizar suas séries')
    if eficacia >= (qtd_exercicios/2):
      if qtd_exercicios%2 == 1 and (qtd_exercicios - eficacia) > eficacia:
        print('NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL')
      else:
        print('ME DEI BEM COM ESSA PLAYLIST, APROVADO')
    else:
      print('NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL')
    eficacia = 0



  