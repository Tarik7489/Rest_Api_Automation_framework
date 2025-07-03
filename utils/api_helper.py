import requests

class APIHelper:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, headers=None, params=None):
        return requests.get(self.base_url + endpoint, headers=headers, params=params)

    def post(self, endpoint, headers=None, json=None):
        return requests.post(self.base_url + endpoint, headers=headers, json=json)

    def put(self, endpoint, headers=None, json=None):
        return requests.put(self.base_url + endpoint, headers=headers, json=json)

    def patch(self, endpoint, headers=None, json=None):
        return requests.patch(self.base_url + endpoint, headers=headers, json=json)

    def delete(self, endpoint, headers=None):
        return requests.delete(self.base_url + endpoint, headers=headers)
