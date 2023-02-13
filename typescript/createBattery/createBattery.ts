import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("E-MAIL", "PASSWORD");

    const batteryType = await apiClient.getBatteryTypeById(
      "BATTERY_TYPE_ID" // check in the Service Center or fetch after youve created your battery type
    );

    // In order to create a battery you need to define Partial<TBattery> object where name and battery type are mandatory
    const createdBattery = await apiClient.createBattery({
      name: "NAME", // you can choose, should be clever maybe you have a lot of batteries in the future
      battery_type: batteryType,
    });

    console.log(createdBattery);
  } catch (e: any) {
    console.error(e.details);
  }
})();
