from configuration import *
from credentials import *
from faker import Factory
from helper import *
from mentifi_api import AuthConnection

config = APIConfigConnection()
auth_conf = AuthConfig()
user = config.user_data()
util = Util()


class DashboardAPI(AuthConnection):

    def __init__(self):
        super().__init__()

    def get_dashboard(self):

        url =  "Users/{}/Dashboards".format(4137)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_whats_happening(self):

        url =  "Users/{}/WhatsHappening".format(4137)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response



if __name__ == "__main__" :
    dashboard = DashboardAPI()
    util.json_parser(dashboard.get_whats_happening())








