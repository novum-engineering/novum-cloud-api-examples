import { APIClient } from "novum-cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    console.log(
      `ID authenticated. You are using the ${user.profile.name}'s account`
    );
    await apiClient.logout();
  } catch (e) {
    console.error(e);
  }
})();
