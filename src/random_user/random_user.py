import requests


class RandomUser:
    def __init__(self):
        self.api_call = 'https://randomuser.me/api/?exc=picture'

    def get_random_user(self):
        response = requests.get(self.api_call)
        if response.ok:
            return response.json()['results'][0]
        else:
            return None

    def get_random_users(self, results):
        response = requests.get(self.api_call+'&results={}'.format(results))
        return response.json()['results']

    def get_random_user_of_given_gender(self, gender):
        if gender != 'female' and gender != 'male':
            raise ValueError('gender must be female or male')
        response = requests.get(self.api_call+'&gender={}'.format(gender))
        return response.json()['results'][0]
