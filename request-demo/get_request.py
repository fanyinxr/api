import requests
import json

URL= 'https://api.github.com'

#url拼接
def bulid_url(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)


def request_method():
    response = requests.get(bulid_url('users/haotest'))

    print(better_output(response.text))


if __name__=='__main__':
    request_method()