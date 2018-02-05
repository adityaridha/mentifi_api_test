from configuration import *
from credentials import *
from faker import Factory
from helper import *
from mentifi_api import AuthConnection

config = APIConfigConnection()
auth_con = AuthConfig()
user = config.user_data()
util = Util()


class AccountAPI(AuthConnection):

    def __init__(self):
        super().__init__()

    def forgot_password(self):

        email = "testmentifi+besswill@gmail.com"
        url = "password/GenerateResetToken?email={}&loginUrl=http://localhost:60000/Account/Login?ReturnUrl=%2F".format(email)

        response = auth_con.auth_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_profile(self):
        url =  "Profile"
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_profile_bio(self, sys_uid=4137):

        url =  "Profile/{}".format(sys_uid)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response

    def get_profile_setting(self, sys_uid=4138):

        url =  "Profile/{}/Setting".format(sys_uid)
        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header)

        return response





if __name__ == "__main__":
    account = AccountAPI()
    # util.json_parser(account.forgot_password())
    util.json_parser(account.get_profile())