num_limite = int(input('Digite um limite para saber os primos: '))
lista_primos = []
for x in range(num_limite, 0, -1):
    quantidade_divisores = 0
    for y in range(num_limite, 0, -1):
        if x % y == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 2:
        lista_primos.append(x)

lista_primos.sort()
print(f'Lista de números primos entre \033[32m1 e {num_limite}:\033[m \n'
      f'{lista_primos}')