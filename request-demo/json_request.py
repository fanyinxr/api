import json

import requests

URL = "https://api.github.com"

def build_url(endpoint):
    #拼接接口请求地址
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def json_method():
    response = requests.patch(build_url('user'),auth=('1666927060@qq.com','20111997ruru'),json={'company':
                                                                                    'haotest',
                                                                                    'email':'1666927060@qq.com'})
    # response = requests.get(bulid_url('user'),auth=('lihanhuan@haotest.com','lihanhuan123'),json={'company'})


    print(better_output(response.text))


if __name__ == '__main__':
    json_method()
