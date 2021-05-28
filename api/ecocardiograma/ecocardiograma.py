def get_ecocardiograma(sheet):
  result = list()
  filtered_sheet = list(filter(lambda x: len(x) == 12, sheet))

  for p in filtered_sheet:
    period = dict()

    period['Data'] = p[2]

    if p[8] == 'Não Cadastrado':
        period['Médico'] = p[9]
    else:
        period['Médico'] = p[8]

    period['E-Mail'] = p[1]

    period['Especialidade'] = 'ECOCARDIOGRAMA'

    period['Período'] = p[10]

    period['Unidade'] = p[11]

    period['Quantidade de Exames'] = int(p[6])

    if p[10] == 'Sábado Tarde':
        period['Valor Bruto'] = 932
        period['Valor Líquido'] = 750
    elif p[10] == 'Domingo Manhã':
        period['Valor Bruto'] = 1100
        period['Valor Líquido'] = 750
    elif p[10] == 'Domingo 12 Horas':
        period['Valor Bruto'] = 1500
        period['Valor Líquido'] = 1207
    elif p[10] == 'BIP':
        period['Valor Bruto'] = int(p[6]) * 300
        period['Valor Líquido'] = int(p[6]) * 241
    elif p[10] == 'Intraoperatório':
        period['Valor Bruto'] = int(p[6]) * 1100
        period['Valor Líquido'] = int(p[6]) * 885.17
    else:
        if int(p[6]) <= 10:
            period['Valor Bruto'] = 1100
        else:
            period['Valor Bruto'] = 1100 + ((int(p[6]) - 10) * 100)

        if int(p[6]) <= 12:
            period['Valor Líquido'] = 750
        else:
            period['Valor Líquido'] = 750 + ((int(p[6]) - 12) * 55)


    result.append(period)

  return result