from novum_api_client.client import NovumAPIClient
from novum_api_client.api_type import TBatteryTypeRequired

api = NovumAPIClient()

try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    # In order to create a battery type you need to define a TBatteryTypeRequired object where name, manufacturer, nominal_voltage and nominal_capacity are mandatory.
    create_battery_type = api.create_battery_type(
        TBatteryTypeRequired(
            name="NAME",  # You can choose an unique name.
            manufacturer="BATTERY_PRODUCER",
            nominal_voltage=3.6,  # in SI unit of Volts
            nominal_capacity=10,  # in Ampere hours (Ah)
        )
    )
    print("A new battery type was created.")

except:
    raise Exception("It was not possible to create a new battery type.")
