import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");

    // In order to query your battery you have 3 optional arguments to use: filters, options and fields as arguments
    const filters = { name: "MY_BATTERY" }; //  any {[key: string]: any;}
    const options = { limit: 100 }; //{ sort?: { [key: string]: number },limit?: number,offset?: number}
    const fields = {}; // any {[key: string]: number};
    const batteries = await apiClient.getBatteries(filters, options, fields);

    console.log(batteries);
  } catch (e: any) {
    console.error(e.details);
  }
})();
