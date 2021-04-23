vproduto= float(input('Digite o valor do produto R$:'))
desconto = float(input('Digite o valor do desconto em %:'))
res = vproduto - ((vproduto * desconto)/100)
print('O produto custa R${} \n Aplicando um desconto de {}% \n O valor final é : R${:.2f}'.format(vproduto,desconto,res))