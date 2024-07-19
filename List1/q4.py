plh = int(input())
clh = int(input())
pmv = int(input())
cmv = int(input())
pvb = int(input())
cvb = int(input())

if clh <= 10:
  plh = plh + 5
if cmv <= 10:
  pmv = pmv + 5
if cvb <= 10:
  pvb = pvb + 5

if plh >= pmv and  plh >= pvb:
  print(f'Lewis Hamilton ganhou a competição com {plh} pontos!')
elif pmv > plh and pmv >= pvb:
  print(f'Max Verstappen ganhou a competição com {pmv} pontos!')
else:
  print(f'Valtteri Bottas ganhou a competição com {pvb} pontos!')