larg=float(input('Digite a Largura de sua parede em metros: '))
alt=float(input('Digite a altura de sua parede em metros : '))
area = larg * alt
tinta = (area/2)
print('Sua parede tem a dimensão de {}X{}m² e sua área é de {}m²\n Será necessário {} litros de tinta'.format(larg,alt,area,tinta))

