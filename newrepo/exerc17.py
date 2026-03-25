print('{:=^40}'.format('LOJINHAS DO JAO'))
preço = float(input('Preço das suas compras: R$'))
print("""FORMAS DE PAGAMENTO
      [ 1 ] à vista no dinheiro
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão""")
opção = int(input('Qual sua opção? '))
if opção == 1:
    opc1 = preço - (preço * 10 / 100) # 10 POR cento!!! 
    print('Sua opção foi à vista no dinheiro, e com 10% de desconto sua compra fica R${:.2f}'.format(opc1))
elif opção == 2:
    opc2 = preço - (preço * 5 / 100) # 5 POR cento!!!!
    print('Sua opção foi à vista no cartão, e com 5% de desconto sua compra fica R${:.2f}'.format(opc2))
elif opção == 3:
    opc3 = preço / 2 # preço da compra, DIVIDIDA em duas parcelas.
    print ('''Sua compra parcelada em 2x no cartão ficará R${:.2f}
           Sendo cada parcela R${:.2f}'''.format(preço, opc3))
else:
    opc4 = preço + (preço * 20 / 100)
    parcelas = int(input('Quantas parcelas voce vai querer?'))
    juros = opc4 / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS '.format(parcelas, juros))
    print('Sua compra de R${:.2f} custará R${:.2f} no final.'.format(preço, opc4))
    