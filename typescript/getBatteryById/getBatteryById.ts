import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("E-MAIL", "PASSWORD");

    // In order to get the "id" of the require battery one can do that copying the id from the Service Center or querying your battery and get its id
    const battery = await apiClient.getBatteryById("DATABASE_ID");
    console.log(battery);
  } catch (e: any) {
    console.error(e.details);
  }
})();
