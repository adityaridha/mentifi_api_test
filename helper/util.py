import json

class Util():

    def print_response(self, response, verbose = False ) :
        print("\n### Status Code : {}".format(response.status_code))
        assert response.status_code == 200, print(response.text)
        if verbose == True :
            print("\n#### Header :")
            print(response.headers)
            print("\n#### Body :")
            print(response.text)

    def json_parser(self, data):
        print("status code : {}".format(data.status_code))
        data_text = data.text
        if data_text == "":
            print("No Data Body")
        else:
            parsed = json.loads(data_text)
            print(json.dumps(parsed, indent=4, sort_keys=True))





