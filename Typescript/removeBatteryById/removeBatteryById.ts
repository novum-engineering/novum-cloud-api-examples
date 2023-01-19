import { APIClient } from "novum-cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    // In order to delete a battery you need to get the "id" of the require battery
    // one can do that copying the id from the Service Center or querying your battery and get its id
    const answer = await apiClient.removeBatteryById("BATTERY_ID");
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
