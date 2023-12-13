from novum_api_client.client import NovumAPIClient

api = NovumAPIClient()

try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    # In order to get the "id" of the require battery one can do that copying the id from the Service Center or querying your batteries and getting their id
    get_battery = api.get_battery_by_id("YOUR_BATTERY_ID")
    battery_name = get_battery.name
    print(f"Your battery named {battery_name} was fetched from our database.")

except:
    raise Exception("It was not possible to fetch your battery.")
