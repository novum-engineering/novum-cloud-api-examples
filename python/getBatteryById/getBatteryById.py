from NovumApiClient.apiClientPublic import NovumBatteriesClient

api = NovumBatteriesClient('')


try:
  login = api.login('YOUR_EMAIL', 'YOUR_PASSWORD')
  #In order to get the "id" of the require battery one can do that copying the id from the Service Center or querying your battery and get its id
  get_battery = api.get_battery_by_id('YOUR_BATTERY_ID') 
  
except:
   raise Exception('It was not possible to fetch your battery.')

