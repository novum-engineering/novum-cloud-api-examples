from novum_api_client.api_type import (
    TInsights,
    TBatteryReading,
    TTreeProperties,
    TBatteryRequired,
)
from novum_api_client.client import NovumAPIClient

api = NovumAPIClient()

try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    # In order to get the "id" of the require battery one can do that copying the id from the Service Center or querying your battery and get its id
    parent_battery = api.get_battery_by_id("YOUR_BATTERY_ID")
    enable_parent = TBatteryReading(
        name=parent_battery.name,
        battery_type=parent_battery.battery_type,
        id=parent_battery.id,
        insights=TInsights(enabled=True),
    )
    update = api.update_battery(enable_parent)
    # after the parent battery is enable to get children, one can create batteries like the following:
    children_battery = api.create_battery(
        TBatteryRequired(
            name="First Cell",
            tree=TTreeProperties(parent=parent_battery.id),
            battery_type=parent_battery.battery_type,
    )
    )

except:
    raise Exception("It was not possible to fetch your battery.")
