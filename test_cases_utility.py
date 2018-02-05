import pytest
import requests
from helper import *
from mentifi_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute Utility test cases #########")


class TestUtility():

    util = Util()

    @pytest.mark.get_only
    def test_time_zone(self):
        result = config.api_request(service_url='Utility/TimeZoneList', request_type="GET")
        self.util.print_response(result)
