import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");

    // In order to create a battery Type you need to define  Partial<TBattery> object where name, manufacturer, nominal_voltage, nominal_capacity are mandatory
    const batteryType = await apiClient.createBattery({
      name: "BATTERY_TYPE", // you can choose, should be clever maybe you have a lot of battery types in the future
      manufacturer: "BATTERY_PRODUCER",
      nominal_voltage: 3.6, // in SI unit of Volts
      nominal_capacity: 10, // in Ampere hours (Ah)
    });

    console.log(batteryType);

  } catch (e: any) {
    console.error(e.details);
  }
})();
