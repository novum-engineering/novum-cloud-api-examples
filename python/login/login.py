from NovumApiClient.NovumApiClient import NovumBatteriesClient

api = NovumBatteriesClient('')

try:
  login = api.login('YOUR_EMAIL', 'YOUR_PASSWORD')
  print(f"ID authenticated. You are using the {login['profile']['email']}s account")
except:
   raise Exception("Login was not possible")

