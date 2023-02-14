import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("E-MAIL", "PASSWORD");
    // In order to update information of a battery you need to define Partial<TBattery> object where id is mandatory
    const parentBattery = await apiClient.getBatteryById("BATTERY_ID");
    const NEST_BATTERY = {
      id: parentBattery.id,
      "tree.enabled": true,
      "insights.enabled": true,
    };
    const update = await apiClient.updateBattery(NEST_BATTERY);
    // after the parent battery is enable to get childrens, one can create batteries like the following:
    const childrenBattery = await apiClient.createBattery({
      name: "First children",
      "tree.parent": parentBattery.id,
      battery_type: parentBattery.battery_type,
    });
    console.log(childrenBattery);
  } catch (e) {
    console.error(e);
  }
})();
