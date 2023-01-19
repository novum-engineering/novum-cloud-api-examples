import { APIClient, genMongoId } from 'novum-cloud-api-client';

console.log(genMongoId(12));

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login('YourEMail', 'YourPassword');

    const batteryTypes = await apiClient.getBatteryTypes();
    console.log(batteryTypes);

    await apiClient.logout();

  } catch (e) {
    console.error(e);
  }
})();
