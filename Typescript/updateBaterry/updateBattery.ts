import { APIClient } from "novum-cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    // In order to update information of a battery you need to define Partial<TBattery> object where id is mandatory
    const NEW_BATTERY_DATE = {
      id: "pQSFbM55v8BjfdCfo",
      name: "NAME_UPDATE_BATTERY",
    };
    const answer = await apiClient.updateBattery(NEW_BATTERY_DATE);
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
