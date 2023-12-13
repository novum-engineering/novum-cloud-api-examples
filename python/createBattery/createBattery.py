from novum_api_client.client import NovumAPIClient
from novum_api_client.api_type import TBatteryEssentials

api = NovumAPIClient()

try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    get_battery_type = api.get_battery_types_by_id(
        "BATTERY_TYPE_ID"
    )  # Check in the Service Center or fetch after youve created your battery type.
    print("My battery type:", get_battery_type)
    # In order to create a battery you need to define a TBatteryEssentials object where name and battery type are mandatory.
    create_battery = api.create_battery(
        TBatteryEssentials(
            name="NAME",  # You should choose an unique name.
            battery_type=get_battery_type,
        )
    )
    print("A new battery was created.")

except:
    raise Exception(f"It was not possible to create a new battery.")