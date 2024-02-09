def primo(n):
    qtd_divisores = 0
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            qtd_divisores += 1
        divisor += 1
    if qtd_divisores == 2:
        return True
    else:
        return False
ehPrimo = int(input('Digite um número e descubra se é primo: '))
if primo(ehPrimo):
    print('É primo!')
else:
    print('Não é primo!')


