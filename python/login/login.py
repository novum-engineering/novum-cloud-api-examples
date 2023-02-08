from NovumApiClient.NovumApiClient import NovumApiClient

api = NovumApiClient('')

login = api.login('l.biz@novum-engineering.com', 'Amsdsdsd')
#print(f'ID authenticated. You are using the {login['profile.name']}s account')

'''

(async () => {
  try {
    const user = await apiClient.login("YOUR_EMAIL", "YOUR_PASSWORD");
    apiClient._setUser(user);
    console.log(
      `ID authenticated. You are using the ${user.profile.name}'s account`
    );
    await apiClient.logout();
  } catch (e: any) {
    console.error(e.details);
  }
})();'''