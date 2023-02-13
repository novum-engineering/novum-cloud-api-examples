from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('E-MAIL', 'PASSWORD')
  # this function alloww you to define filters and options
  filters = { 'name': "NAME" } #  any {[key: string]: any;}
  options = { 'limit': 100 } #{ sort?: { [key: string]: number },limit?: number,offset?: number}

  batteries = api.get_batteries(filters, options);
  print(batteries)
except:
   raise Exception(f'It was not possible to fetch your battery.')

