km=float(input('Digite um valor em Kilometro: '))
hm= km /     10
dam=km /    100
m= km /    1000
dm= km /  10000
cm= km / 100000
mm= km /1000000

print ('O valor de Quilometros é:{} \n Convertido para Hectomero é: {} '
       '                            \n Convertido para Dêcametro é: {} '
       '                            \n convertido para Metros é:    {} '
       '                            \n Convertido para Decímetro é: {} '
       '                            \n Convertido para Centímetro é:{} '
       '                            \n Convertido para milímetros é:{}'.format(km,hm,dam,m,dm,cm,mm))

