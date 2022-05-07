from time import sleep
termos = []
total_med = int(input('Digite o total de termos para o cálculo: '))
if total_med <= 0:
    print('Quantia de termos inválida!')
for caracter in range(0, total_med):
    valor = float(input(f'Digite o {caracter + 1}° termo: '))
    termos.append(valor)
termos.sort()
print('Calculando...\n')
sleep(2.2)
if total_med % 2 == 0:
    elemento_1 = int(total_med / 2)
    elemento_2 = int(total_med / 2 + 1)
    calculo = (termos[elemento_1 - 1] + termos[elemento_2 - 1]) / 2
    print(f'A mediana dos termos apresentados é representada por:{calculo}.')
else:
    elemento_1 = int(total_med / 2)
    print(f'A mediana dos termos apresentados é representada por:{termos[elemento_1]}')