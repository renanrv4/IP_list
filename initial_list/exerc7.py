diamonds = [10, 30, 100]
names = ['Arthur', 'Luiz', 'Pedro']

drequired = int(input())

for x in range(len(names)):
  if x > len(names):
    break
  if drequired > diamonds[x-1]:
    del names[x-1]
    del diamonds[x-1]
    
if drequired <= diamonds[0]:
  print(names[0])
else:
  print('Nenhum')
