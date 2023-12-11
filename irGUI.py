# Interface Gráfica do Projeto IR

import PySimpleGUI as psg

import ir

layout = [
    [psg.Text('Informe o salário: '), psg.InputText('', key='salarioBruto', size=17)],
    [psg.Text('Núm. de dependentes: '), psg.InputText('', key='numDependentes', size=12)],
    [psg.Check('A partir de maio de 2023?', key='regraAtual')],
    [psg.Button('Calcular'), psg.Button('Limpar')],
    [psg.Text('-'*50)],
    [psg.Text('', key='salarioBase')],
    [psg.Text('', key='taxa')],
    [psg.Text('', key='irDevido')],
    [psg.Text('-'*50)],
    [psg.Text('', key='salarioLiquido')],
    [psg.Text('', key='taxaEfetiva')],
]

janela = psg.Window('Simulador do IRPF', layout)

while True:
    evento, valor = janela.read()

    if evento == psg.WIN_CLOSED:
        break
    elif evento == 'Limpar':
        janela['salarioBruto'].update('')
        janela['numDependentes'].update('')
        janela['salarioBase'].update('')
        janela['taxa'].update('')
        janela['irDevido'].update('')
        janela['salarioLiquido'].update('')
        janela['taxaEfetiva'].update('')
        janela['salarioBruto'].set_focus()
        janela['regraAtual'].update(False)
    else:
        regra = valor['regraAtual']
        imposto = ir.imposto(float(valor['salarioBruto']), int(valor['numDependentes']), regra)
        janela['salarioBase'].update('Salário Base...........R$ {:.2f}'.format(imposto['salarioBase']))
        janela['taxa'].update('Alíquota.......................{:.2f}%'.format(imposto['taxa']*100))
        janela['irDevido'].update('IR Devido..................R$ {:.2f}'.format(imposto['irDevido']))
        janela['salarioLiquido'].update('Salário Líquido...........R$ {:.2f}'.format(imposto['salarioLiquido']))
        janela['taxaEfetiva'].update('Alíquota Efetiva...................{:.2f}%'.format(imposto['taxaEfetiva']*100))

janela.close()