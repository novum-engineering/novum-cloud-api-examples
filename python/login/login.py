from novum_api_client.client import NovumAPIClient

api = NovumAPIClient()

try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    my_name = login.profile["name"]
    print(f"ID authenticated. You are using the {my_name}'s account")
except:
    raise Exception("Login was not possible")