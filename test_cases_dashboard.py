import pytest
import allure
from helper import *
from mentifi_api import *

__author__      = "Muhammad Aditya Ridharrahman"
__version__     = "1.0"
__email__       = "aditya.ridharrahman@geekseat.com.au"
__status__      = "development"
__last_update__ = "10th Feb 2017"

print("######### Execute dashboard test cases #########")

@allure.severity(pytest.allure.severity_level.CRITICAL)
class TestDashboard():

    dashboard_api = DashboardAPI()
    util = Util()

    @pytest.mark.get_only
    def test_dashboard(self):
        result = self.dashboard_api.get_dashboard()
        self.util.print_response(result, verbose=True)

    # def test_pending_invitation(self):
    #     pass
    #
    # def test_connect_request(self):
    #     pass
