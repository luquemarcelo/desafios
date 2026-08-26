#Problema Zero
'''
Números quadrados de inteiros positivos são eles multiplicados por eles mesmos. Por exemplo, 1² = 1, 2² = 4, 3² = 9, 4² = 16, 5² = 25 e assim por diante.
Os 5 primeiros quadrados de inteiros positivos são 1, 4, 9, 16 e 25. A soma desses números é 55.
A soma dos ímpares desses primeiros quadrados de inteiros positivos é 1 + 9 + 25 = 35.
Encontre a soma dos ímpares dos primeiros 823.000 quadrados de inteiros positivos.
'''

numero = 1
expoente = 2
somatorio = 0
for num in range(1, 823001):
    resultado = numero ** expoente
    if resultado%2 == 1:
        somatorio += resultado
    numero += 1
print(f"o somatório é {somatorio}")
