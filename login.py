import requests


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer':'https://github.com/',
        },
        self.post_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self .logined_url = 'https://github.com/settings/profile'
        self. session = requests.Session()
