# Processamento do sistema

def imposto(salarioBruto, dependentes, novaRegra):
    # Calculo do desconto por dependente
    descontoDependentes = dependentes * 189.59

    if descontoDependentes < 528 and novaRegra:
        # Desconto simplificado
        salarioBase = salarioBruto - 528

        # Tabela atual
        if salarioBase < 2112:
            aliquota = 0.0
            descontoFaixa = 0.0
        elif salarioBase <= 2826.65:
            aliquota = 0.075
            descontoFaixa = 158.4
        elif salarioBase <= 3751.05:
            aliquota = 0.15
            descontoFaixa = 370.4
        elif salarioBase <= 4664.68:
            aliquota = 0.225
            descontoFaixa = 651.73
        else:
            aliquota = 0.275
            descontoFaixa = 884.96
    else:
            # Desconto por dependente
        salarioBase = salarioBruto - descontoDependentes

        # Tabela atual
        if salarioBase < 1903.98:
            aliquota = 0.0
            descontoFaixa = 0.0
        elif salarioBase <= 2826.65:
            aliquota = 0.075
            descontoFaixa = 142.8
        elif salarioBase <= 3751.05:
            aliquota = 0.15
            descontoFaixa = 354.8
        elif salarioBase <= 4664.68:
            aliquota = 0.225
            descontoFaixa = 636.13
        else:
            aliquota = 0.275
            descontoFaixa = 869.36


    impostoBruto = salarioBase * aliquota
    irDevido = impostoBruto - descontoFaixa
    salarioLiquido = salarioBruto - irDevido
    aliquotaEfetiva = irDevido/salarioBruto

    return {
        'salarioBruto': salarioBruto,
        'dependentes': dependentes,
        'salarioBase': salarioBase,
        'taxa': aliquota,
        'irDevido': irDevido,
        'salarioLiquido': salarioLiquido,
        'taxaEfetiva': aliquotaEfetiva
    }