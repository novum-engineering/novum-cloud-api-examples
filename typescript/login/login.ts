import { PublicAPIClient as APIClient } from "@novum-batteries/cloud-api-client";

const apiClient = new APIClient();

(async () => {
  try {
    const user = await apiClient.login("E-MAIL", "PASSWORD");

    apiClient._setUser(user);
    console.log(
      `ID authenticated. You are using the ${user.profile.name}'s account`
    );
    await apiClient.logout();
  } catch (e: any) {
    console.error(e.details);
  }
})();
