from novum_api_client.client import NovumAPIClient

api = NovumAPIClient()

try:
    login = api.login("YOUR_EMAIL", "YOUR_PASSWORD")
    # This function allow you to define filters, options and fields
    filters = {"name": "NAME"}  # any {[key: string]: any;}
    options = {
        "limit": 100
    }  # { sort?: { [key: string]: number },limit?: number,offset?: number}

    batteries = api.get_batteries(filters, options)
    print("My batteries:",batteries)
except:
    raise Exception(f"It was not possible to fetch your battery.")
