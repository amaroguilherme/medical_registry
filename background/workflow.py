from background.connection import get_connection
from settings import SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME
from api.ecocardiograma.ecocardiograma import get_ecocardiograma

def format_production():
  sheet = get_connection()

  result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
  values = result.get('values', [])

  result_eco = get_ecocardiograma(values)

  return result_eco