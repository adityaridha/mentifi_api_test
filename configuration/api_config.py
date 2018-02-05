import requests
from requests.exceptions import ReadTimeout
import credentials

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "12th December 2017"


class APIConfigConnection():

    def __init__(self):
        pass

    # need below property tag, unless it will be called as object
    @property
    def address(self):
        TEST = "http://54.252.243.118:6002/api/"
        # BASE_URL = "http://54.206.127.216:6002/api/"
        return TEST

    def user_data(self):
        user = credentials.Mentee()
        return user

    @property
    def post_header(self):
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        return headers

    def api_request(self, service_url, custom_headers=None, data_body=None , params=None, request_type = "POST"):

        if request_type == "POST" :
            request_result = requests.post(url=self.address + service_url, data=data_body, headers=custom_headers)
        elif request_type == "PUT":
            request_result = requests.put(url=self.address + service_url, data=data_body, headers=self.post_header)
        elif request_type == "GET":
            request_result = requests.get(url=self.address + service_url, headers=custom_headers, params=params, timeout=20)
        else:
            request_result = None

        return request_result



class AuthConfig(APIConfigConnection):

    def __init__(self):
        super().__init__()

    @property
    def auth_address(self):
        TEST = "https://test-auth-d2kluue7bb.hub3c.com/"
        BASE_URL = TEST

        return BASE_URL

    def auth_request(self, service_url, custom_headers=None, data_body=None , request_type = "POST"):

        if request_type == "POST" :
            request_result = requests.post(url=self.auth_address + service_url, data=data_body, headers=custom_headers)

        elif request_type == "GET":
            request_result = requests.get(url=self.auth_address + service_url, headers=custom_headers)
        else :
            request_result = None

        return request_result


if __name__ == "__main__" :

    con = AuthConfig()
    print(con.address)

    # data = {"client_id":"ios-app",
    #         "client_secret":"ZXasqw12",
    #         "grant_type":"client_credentials",
    #         "scope":"auth-api"}
    #
    # result = con.auth_request(service_url="connect/token", data_body=data, request_type="POST")
    # token = result.json()['access_token']


