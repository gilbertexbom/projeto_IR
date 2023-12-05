# Sistema para recolhimento de IR com base no salário

# Apresentação
print('\n\t\t\t -- Sistema para Recolhimento de IRPF --\n')

# Entradas
salarioBruto = float(input('Informe o salário: '))
dependentes = int(input('Informe o número de dependentes: '))

# Processamento
descontoDependentes = dependentes * 189.59
salarioBase = salarioBruto - descontoDependentes

if salarioBase < 1903.98:
    aliquota = 0.0
    descontoFaixa = 0.0
elif salarioBase <= 2826.65:
    aliquota = 0.075
    descontoFaixa = 142.8
elif salarioBase <= 3751.05:
    aliquota = 0.15
    descontoFaixa = 354.8
elif salarioBase <= 4664.8:
    aliquota = 0.225
    descontoFaixa = 636.13
else:
    aliquota = 0.275
    descontoFaixa = 869.36

impostoBruto = salarioBase * aliquota
irDevido = impostoBruto - descontoFaixa
salarioLiquido = salarioBruto - irDevido
aliquotaEfetiva = irDevido/salarioBruto

print('\n\t\t\t -- Dados do IR --\n')
print('Salário Bruto..............R$ {:.2f}'.format(salarioBruto))
print('Núm. de dependentes.................{}'.format(dependentes))
print('-'*40)
print('Salário Base................R$ {:.2f}'.format(salarioBase))
print('Alíquota........................{:.2f}%'.format((aliquota*100)))
print('IR Devido...................R$ {:.2f}'.format(irDevido))
print('-'*40)
print('Salário Líquido.............R$ {:.2f}'.format(salarioLiquido))
print('Alíquota Efetiva................{:.2f}%'.format((aliquotaEfetiva*100)))









