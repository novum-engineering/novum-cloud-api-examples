import { APIClient } from "novum-cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    // In order to create a battery you need to define Partial<TBattery> object where name, battery type are mandatory
    const BATTERY_TYPE_ID = await apiClient.getBatteryTypeById(
      "BATTERY_TYPE_ID" // check in the Service Center or take after create you battery type
    );
    const MY_BATTERY_DATE = {
      name: "MY_BATTERY",
      battery_type: BATTERY_TYPE_ID,
    };

    const answer = await apiClient.createBattery(MY_BATTERY_DATE);
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
