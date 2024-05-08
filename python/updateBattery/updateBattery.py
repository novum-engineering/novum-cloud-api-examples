from novum_api_client.client import NovumAPIClient
from novum_api_client.api_type import TBatteryReading

api = NovumAPIClient()
# Here we will update the name of an choosen battery
try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    battery_to_be_update = api.get_battery_by_id("YOUR_BATTERY_ID")
    NEW_BATTERY_DATA = TBatteryReading(
        id=battery_to_be_update.id,
        name="NEW_NAME",
        battery_type=battery_to_be_update.battery_type,
    )
    updated_battery = api.update_battery(NEW_BATTERY_DATA)
    print(updated_battery)

except:
    raise Exception("Your battery was not updated.")
