print('--'*30)
print('\033[37mPRECIFICAÇÃO DE PRODUTO PARA REVENDA\033[m')
print('--'*30)
vc = margem = icmsv = impostos = 0
cicms = ' '
while vc == 0:
    try:
        vc = float(input('Digite o Valor de Compra do Produto: R$ '))
    except:
        print('\033[33mValor Incorreto! Por favor, informe o valor correto\033[m')
while margem == 0:
    try:
        margem = int(input('Digite o Percentual de Margem de Lucro Desejado: '))
    except:
        print('\033[33mMargem Incorreta! Por favor, informe a margem novamente\033[m')
print('''\033[37mEm Qual Regime Tributário está a sua Empresa?
1 para Simples Nacional:
2 para MEI:
3 para Lucro Real:
4 para Lucro Presumido: \033[m''')
regime = list(range(1,5))
while regime not in range (1,5):
    try:
        regime = int(input('Digite o número que corresponde ao Regime Tributário da sua Empresa: '))
        if regime == 1:
            anexo = list(range(1,7))
            while anexo not in range(1,7):
                try:
                    anexo = int(input('Escolha o anexo do Simples Nacional referente ao seu faturamento: '))
                    if anexo == 1:
                        impostos = 4.5
                        break
                    if anexo == 2:
                        impostos = 7.8
                        break
                    if anexo == 3:
                        impostos = 10
                        break
                    if anexo == 4:
                        impostos = 11.20
                        break
                    if anexo == 5:
                        impostos = 14.70
                        break
                    if anexo == 6:
                        impostos = 30
                        break
                    else:
                        print('\033[33mOpção Inválida! Por favor, digite novamente.\033[m')
                except:
                    print('\033[33mAnexo Incorreto! Por favor, informe novamente.\033[m')
            break
        if regime == 2:
            impostos = 0
            break
        if regime == 3:
            while icmsv == 0:
                try:
                    icmsv = int(input('Digite o Percentual de ICMS sobre a Venda: '))
                except:
                    print('\033[33mValor Incorreto! Digite Novamente.\033[m')
            break
        if regime == 4:
            while icmsv == 0:
                try:
                    icmsv = int(input('Digite o Percentual de ICMS sobre a Venda: '))
                except:
                    print('\033[33mValor Incorreto! Digite Novamente.\033[m')
            break
        else:
            print('\033[33mRegime Incorreto! Por favor, Digite Novamente.\033[m')
    except:
        print('\033[33mRegime Incorreto! Por favor, Digite Novamente.\033[m')
if regime == 3:
    while cicms not in 'SN':
        try:
            cicms = str(input('Esta Compra tem Crédito de ICMS? [S/N]: ')).strip().upper()[0]
        except:
            print('\033[33mOpção Inválida! Digite Novamente.\033[m')
    impostos = icmsv + 9.25
if regime == 4:
    while cicms not in 'SN':
        try:
            cicms = str(input('Esta Compra tem Crédito de ICMS? [S/N]: ')).strip().upper()[0]
        except:
            print('\033[33mOpção Inválida! Digite Novamente.\033[m')
    impostos = icmsv + 3.65
if cicms == 'S':
    try:
        icmsc = float(input('Digite o Percentual de ICMS sobre Compra: '))
    except:
        print('\033[33mValor Incorreto! Digite Novamente.\033[m')
    icmsc = icmsc / 100
    custoc = vc - (icmsc * vc)
else:
    custoc = vc
if regime == 1 or regime == 2:
    custoc = vc
vv = (custoc / (100 - (impostos + margem))) * 100
print(f'\033[37mValor de Venda: R$ {vv:.2f}')
print(f'Valor de Compra do Produto (MP): R$ {vc:.2f}')
print(f'O Custo Final da Compra é de R$ {custoc:.2f}')
print(f'Impostos {impostos:.1f}%: R$ {vv*(impostos/100):.2f}')
print(f'Margem de Contribuição / Lucro Bruto {margem:.1f}%: R$ {vv*(margem/100):.2f}\033[m')