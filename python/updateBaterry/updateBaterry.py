from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('YOUR_EMAIL', 'YOUR_PASSWORD')
  NEW_BATTERY_DATE = {
      'id': 'pQSFbM55v8BjfdCfo',
      'name': 'NAME_UPDATE_BATTERY',
    }
  updated_battery = api.update_battery(NEW_BATTERY_DATE)
  print(updated_battery)

except:
   raise Exception('Your battery was not updated.')

