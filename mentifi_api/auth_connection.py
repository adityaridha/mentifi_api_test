from configuration import *
from credentials import *
from faker import Factory
from helper import *

config = APIConfigConnection()
auth_conf = AuthConfig()
user = config.user_data()
util = Util()


class AuthConnection:

    def get_token(self):

        url = "connect/token"

        email = "bezita@mailinator.com"
        password = "ZXasqw12"

        data = {"client_id": "ios-app",
                "client_secret": "ZXasqw12",
                "grant_type": "password",
                "username": "{}".format(email),
                "password":"{}".format(password)}

        response = auth_conf.auth_request(service_url=url, data_body=data, request_type="POST")

        return response

    @property
    def set_header(self):
        token = self.get_token().json()['access_token']
        header = auth_conf.post_header
        header['Authorization'] = 'Bearer ' + token

        return header

if __name__ == "__main__":
    account = AuthConnection()
    util.json_parser(account.get_token())