def ler_numeros():
    numeros = []
    for i in range(5):
        while True:
            try:
                num = int(input(f'Digite o número {i + 1}: '))
                numeros.append(num)
                break
            except ValueError:
                print('Por favor, digite um número inteiro válido.')
    return numeros
