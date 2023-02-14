import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("E-MAIL", "PASSWORD");
    // In order to update information of a battery you need to define Partial<TBattery> object where id is mandatory
    const updateBattery = await apiClient.getBatteryById("BATTERY_ID");
    const NEW_BATTERY_INFO = {
      id: updateBattery.id,
      name: "updated battery",
    };
    const answer = await apiClient.updateBattery(NEW_BATTERY_INFO);
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
