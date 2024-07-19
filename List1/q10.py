x, op, y = int(input()), input(), int(input())
result = x + y if op == '+' else x - y if op == '-' else x * y if op == '*' else x // y if op == '/' else 'Erro: operador não reconhecido.'
print(result)