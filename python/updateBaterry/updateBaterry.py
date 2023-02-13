from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('E-MAIL', 'PASSWORD')
  NEW_BATTERY_DATE = {
      'id': 'CREATE_AN_ID',
      'name': 'NAME_UPDATE_BATTERY',
    }
  updated_battery = api.update_battery(NEW_BATTERY_DATE)
  print(updated_battery)

except:
   raise Exception('Your battery was not updated.')

