from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('E-MAIL', 'PASSWORD')
  '''In order to delete a battery you need to get the "id" of the require battery
     one can do that copying the id from the Service Center or querying your battery and get its id'''
  batterie = api.get_batteries(filter={"name": "NAME"}, option= {"limit": 100})[0]
  print(batterie["id"])
  removed_battery = api.remove_battery_by_id(batterie["id"])


except:
   raise Exception("It was not possible to delete your battery.")

 