num = input()
ordem = len(num)
soma = 0

for digito in num:
    soma += int(digito) ** ordem

if(soma == int(num)):
    print(f'{num} é um numero Armstrong e sua ordem é {ordem}')
else:
    print(f'{num} não é Armstrong')