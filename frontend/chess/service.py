import requests
from requests.auth import HTTPBasicAuth

class InvalidLoginException(Exception):
    pass

class UserNotFoundException(Exception):
    pass

class ChessService:

    def __init__(self, base_url):
        self.base_url = base_url
        self.basic_auth = None

    def signup(self, email, password):
        payload = {'email': email, 'password': password}
        response = requests.post(self.base_url+'/users',json=payload)

        if response.status_code != 200:
            raise RuntimeError('Unexpected Error')
        else:
            self.basic_auth = HTTPBasicAuth(email, password)
        
    def login(self, email, password):
        ba = HTTPBasicAuth(email, password)
        response = requests.get(self.base_url+'/user', auth=ba)

        if response.status_code != 200:
            raise InvalidLoginException
        else: 
            self.basic_auth = ba

    def save_score(self, score, level):
        if self.basic_auth:
            payload = {'score': score, 'level': level}
            response = requests.post(self.base_url+'/scores',json=payload, auth=self.basic_auth)

            if response.status_code != 200:
                raise RuntimeError('Error Saving Score')

    def get_high_score(self):
        response = requests.get(self.base_url+'/scores/top', auth=self.basic_auth)

        if response.status_code != 200:
            raise RuntimeError('Error Getting Score')
        else:
            return response.json()

    def get_leaders(self, level):
        response = requests.get(f"{self.base_url}/users/leaders?level={level}")

        if response.status_code != 200:
            raise RuntimeError('Error Getting Score')
        else:
            return response.json()


