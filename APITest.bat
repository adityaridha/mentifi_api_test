@echo off
pytest -v D:\works\API_automation_script\test_cases_business.py --alluredir report_xml %*
allure generate report_xml -o web_report_test --clean
pause