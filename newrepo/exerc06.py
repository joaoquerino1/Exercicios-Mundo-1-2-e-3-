salario = float(input('Qual é o seu salario?'))
if salario > 1250.00:
    nsalario = salario + (salario * 0.10)
if salario <= 1250.00:
    nsalario = salario + (salario * 0.15)
print('O seu salario sendo {:.2f}, agora passa a ganhar {:.2f}'.format(salario, nsalario))