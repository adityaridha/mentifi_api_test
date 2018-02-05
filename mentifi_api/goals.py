from configuration import *
from credentials import *
from faker import Factory
from helper import *
from mentifi_api import AuthConnection

config = APIConfigConnection()
auth_con = AuthConfig()
user = config.user_data()
util = Util()


class GoalsAPI(AuthConnection):

    def __init__(self):
        super().__init__()

    def get_goals(self):

        url =  "Goals"
        parameter = {"SystemUserId":"{}".format(4294)}

        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header, params=parameter)

        return response


    def post_new_goals(self):

        url =  "Goals"
        data = {"description": "dari Python", "probability": "Easy", "menteeSystemUserId": "4294"}
        response = config.api_request(service_url=url, request_type="POST", custom_headers=self.set_header, data_body=str(data))

        return response



if __name__ == "__main__":

    Goals = GoalsAPI()
    util.json_parser(Goals.get_goals())