from NovumApiClient.apiClientPublic import NovumBatteriesClient

api = NovumBatteriesClient('')


try:
  login = api.login('E-MAIL', 'PASSWORD')
  create_battery_type = api.create_batttery_type({
      'name': "NAME", # you can choose, should be clever maybe you have a lot of battery types in the future
      'manufacturer': "BATTERY_PRODUCER",
      'nominal_voltage': 3.6, #// in SI unit of Volts
      'nominal_capacity': 10, #// in Ampere hours (Ah)
    })

except:
   raise Exception("It was not possible to create a new battery type.")

