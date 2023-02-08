from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('YOUR_EMAIL', 'YOUR_PASSWORD')
  get_battery_type = api.get_battery_types_by_id('SxWzFS3H8wudGugCv') # check in the Service Center or fetch after youve created your battery type
  ##In order to create a battery you need to define Partial<TBattery> object where name and battery type are mandatory
  create_battery = api.create_battery({
      'name': 'NAME_OF_MY_BATTERY', ## you can choose an unique name, should be clever maybe you have a lot of batteries in the future
      'battery_type': get_battery_type
    })
  
except:
   raise Exception(f'It was not possible to create a new battery.')



