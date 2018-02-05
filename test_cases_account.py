import pytest
from helper import *
from mentifi_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th January 2017"

util = Util()

class TestAccount():

    account_api = AccountAPI()
    auth = AuthConnection()
    util = Util()

    def test_login(self):
        result = self.auth.get_token()
        self.util.json_parser(result)

    def test_get_user_bio(self):
        result = self.account_api.get_profile_bio()
        self.util.json_parser(result)



