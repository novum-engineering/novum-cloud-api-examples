import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");

    // In order to delete a battery you need to get the "id" of the require battery
    // one can do that copying the id from the Service Center or querying your battery and get its id    
    const removed = await apiClient.removeBatteryById("BATTERY_ID");
    console.log(removed);

  } catch (e: any) {
    console.error(e.details);
  }
})();
