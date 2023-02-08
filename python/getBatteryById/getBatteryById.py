from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('YOUR_EMAIL', 'YOUR_PASSWORD')
  get_battery= api.get_battery_by_id('8eAugCB4fvmZ4P295') 
  #In order to get the "id" of the require battery one can do that copying the id from the Service Center or querying your battery and get its id
  print(get_battery)
except:
   raise Exception(f'It was not possible to fetch your battery.')

