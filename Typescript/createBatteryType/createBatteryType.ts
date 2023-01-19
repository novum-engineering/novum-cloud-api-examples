import { APIClient } from "novum-cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    // In order to create a battery Type you need to define  Partial<TBattery> object where name, manufacturer, nominal_voltage, nominal_capacity are mandatory
    const MY_BATTERY_TYPE_DATA = {
      name: "BATTERY_TYPE",
      manufacturer: "BATTERY_PRODUCER",
      nominal_voltage: 3.6,
      nominal_capacity: 10,
    };
    const answer = await apiClient.createBattery(MY_BATTERY_TYPE_DATA);
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
