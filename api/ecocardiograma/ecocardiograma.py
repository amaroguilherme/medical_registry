def get_ecocardiograma(sheet):
  result = list()
  filtered_sheet = list(filter(lambda x: len(x) == 12, sheet))

  for p in filtered_sheet:
    period = dict()

    period['data'] = p[2]

    if p[8] == 'Não Cadastrado':
        period['medico'] = p[9]
    else:
        period['medico'] = p[8]

    period['e-mail'] = p[1]

    period['especialidade'] = 'ECOCARDIOGRAMA'

    period['periodo'] = p[10]

    period['unidade'] = p[11]

    period['qt_de_exames'] = int(p[6])

    if p[10] == 'Sábado Tarde':
        period['valor_bruto'] = 932
        period['valor_liquido'] = 750
    elif p[10] == 'Domingo Manhã':
        period['valor_bruto'] = 1100
        period['valor_liquido'] = 750
    elif p[10] == 'Domingo 12 Horas':
        period['valor_bruto'] = 1500
        period['valor_liquido'] = 1207
    elif p[10] == 'BIP':
        period['valor_bruto'] = int(p[6]) * 300
        period['valor_liquido'] = int(p[6]) * 241
    elif p[10] == 'Intraoperatório':
        period['valor_bruto'] = int(p[6]) * 1100
        period['valor_liquido'] = int(p[6]) * 885.17
    else:
        if int(p[6]) <= 10:
            period['valor_bruto'] = 1100
        else:
            period['valor_bruto'] = 1100 + ((int(p[6]) - 10) * 100)

        if int(p[6]) <= 12:
            period['valor_liquido'] = 750
        else:
            period['valor_liquido'] = 750 + ((int(p[6]) - 12) * 55)


    result.append(period)

  return result