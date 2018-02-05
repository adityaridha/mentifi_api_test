from configuration import *
from credentials import *
from faker import Factory
from helper import *
from mentifi_api import AuthConnection

config = APIConfigConnection()
auth_con = AuthConfig()
user = config.user_data()
util = Util()


class TasksAPI(AuthConnection):

    def __init__(self):
        super().__init__()

    def get_pending_tasks(self):

        url =  "Tasks/Pending"
        parameter = {"fromSystemUserId":"{}".format(4294),
                     "toSystemUserId":"{}".format(4137)}

        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header, params=parameter)

        return response

    def get_completed_task(self):
        url =  "Tasks/Completed"
        parameter = {"fromSystemUserId":"{}".format(4294),
                     "toSystemUserId":"{}".format(4137)}

        response = config.api_request(service_url=url, request_type="GET", custom_headers=self.set_header, params=parameter)

        return response

    def post_new_task(self):
        pass



if __name__ == "__main__":

    Task = TasksAPI()
    util.json_parser(Task.get_completed_task())