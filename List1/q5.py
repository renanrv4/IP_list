direcao1 = ''
direcao2 = ''
fr1 = input()
if fr1 == "Tem uma curva vindo aí, me ajuda!":
  direcao1 = input()
fr2 = input()
if fr2 == "Tem uma curva vindo aí, me ajuda!":
  direcao2 = input()

# 1º comando
if fr1 == "TÔ EM ÚLTIMO!":
  print("PISA FUNDO")
elif fr1 == "Esse cara não sai da minha frente...":
  print("Ultrapassa ele agora!")
elif fr1 == "Tem uma curva vindo aí, me ajuda!":
  print("FREIA AGORA E ME DIZ PARA QUE LADO É")
  if direcao1 == 'DIREITA':
    print("ENTÃO VIRA LOGO!")
  elif direcao1 == 'ESQUERDA':
    print("É SÓ VIRAR!")
  else:
    print("Assim não tem como te ajudar, amiga")
elif fr1 == "MEU PNEU FUROU SOCORRO!":
  print("Amiga, calma! Tem um pit stop na tua frente…")
else:
  print("Eita, não entendi nada…")
  
# 2º comando
if fr2 == "TÔ EM ÚLTIMO!":
  print("PISA FUNDO")
elif fr2 == "Esse cara não sai da minha frente...":
  print("Ultrapassa ele agora!")
elif fr2 == "Tem uma curva vindo aí, me ajuda!":
  print("FREIA AGORA E ME DIZ PARA QUE LADO É")
  if direcao2 == 'DIREITA':
    print("ENTÃO VIRA LOGO!")
  elif direcao2 == 'ESQUERDA':
    print("É SÓ VIRAR!")
  else:
    print("Assim não tem como te ajudar, amiga")
elif fr2 == "MEU PNEU FUROU SOCORRO!":
  print("Amiga, calma! Tem um pit stop na tua frente…")
else:
  print("Eita, não entendi nada…")

print("LET'S RIDE!")




