from configuration import *
from credentials import *
from faker import Factory
from helper import *
from mentifi_api import AuthConnection

config = APIConfigConnection()
auth_conf = AuthConfig()
user = config.user_data()
util = Util()


class NetworksAPI(AuthConnection):

    def __init__(self):
        super().__init__()

    def get_connected_network(self):

        url =  "Networks/{}/Connected".format(4137 )
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_requested_network(self):

        url =  "Networks/{}/Requested".format(4138)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_pending_network(self):

        url =  "Networks/{}/Pending".format(4137)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_all_mentee(self):

        url = "Mentees/{}".format(4137)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_all_mentors(self):

        url = "Mentors/{}".format(4138)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response


if __name__ == "__main__":

    network = NetworksAPI()
    util.json_parser(network.get_connected_network())
    #
    #
    # elements = range(2,10,1)
    # for element in elements:
    #     print(element,end="")