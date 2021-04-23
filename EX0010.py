# -- considere 1 dolar valor 3.27 --

valor=float(input('Digite o valor em real que tu tens na carteira: R$'))
dollar = (valor/3.27)
print('O valor em real que tu tens na carteira é: R${} \n Este valor convertido em dollar seria: ${:.2f}'.format(valor,dollar))