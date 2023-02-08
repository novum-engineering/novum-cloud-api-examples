from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('YOUR_EMAIL', 'YOUR_PASSWORD')
  # this function alloww you to define filters and options
  filters = { 'name': "NAME_OF_MY_BATTERY" } #  any {[key: string]: any;}
  options = { 'limit': 100 } #{ sort?: { [key: string]: number },limit?: number,offset?: number}

  batteries = api.get_batteries(filters, options);
  print(batteries)
except:
   raise Exception(f'It was not possible to fetch your battery.')

