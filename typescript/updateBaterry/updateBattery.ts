import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("E-MAIL", "PASSWORD");
    // In order to update information of a battery you need to define Partial<TBattery> object where id is mandatory
    const NEW_BATTERY_DATE = {
      id: "DATABASE_ID",
      name: "NAME_UPDATE_BATTERY",
    };
    const answer = await apiClient.updateBattery(NEW_BATTERY_DATE);
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
