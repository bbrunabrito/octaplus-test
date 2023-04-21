num1 = float(input())
num2 = float(input())
num3 = float(input())

maior = num1

if maior < num2:
    maior = num2

if maior < num3:
    maior = num3

print(f'{maior} é o maior número ')