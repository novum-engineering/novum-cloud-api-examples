import { APIClient } from "novum-cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    // In order to query your battery you have 3 optinal arguments to use: filters, options and fields as arguments
    const filters = { name: "MY_BATTERY" }; //  any {[key: string]: any;}
    const options = { limit: 100 }; //{ sort?: { [key: string]: number },limit?: number,offset?: number}
    const fields = {}; // any {[key: string]: number};
    const answer = await apiClient.getBatteries(filters, options, fields);
    console.log(answer);
  } catch (e) {
    console.error(e);
  }
})();
