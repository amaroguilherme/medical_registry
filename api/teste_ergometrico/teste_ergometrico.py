# def get_teste_ergometrico(sheet):
#   result = list()

#   for p in sheet:
#     period = dict()

#     period['Data'] = p[2].strftime("%d/%m/%Y")

#     period['Médico'] = p[8]
#     period['E-Mail'] = p[1]
#     period['Especialidade'] = 'TESTE ERGOMÉTRICO'
#     period['Período'] = 'N/E'
#     period['Unidade'] = row['Unidade']
#     period['Quantidade de Exames'] = row['Quantidade de Exames']

#     if row['Unidade'] == 'Itaim/Vila Nova Star':
#         period['Valor Bruto'] = 1050
#         period['Valor Líquido'] = 840

#     elif row['Unidade'] == 'Morumbi':
#         period['Valor Bruto'] = 950
#         period['Valor Líquido'] = 750

#     result.append(period)