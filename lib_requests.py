"""
    Get, Post gibi curl ile yapılan isteklerin python requests kütüphanesini
    kullanarak gerçekleştirilmesini inceleyeceğiz.
"""

import requests

# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' https://hooks.slack.com/services/asdfasdfasdf

headers = {
    'Content-type': 'application/json',
}
data = '{"text":"Hello, World!"}'
response = requests.post('https://hooks.slack.com/services/asdfasdfasdf',
                         headers=headers, data=data)


# curl -d @request.json --header "Content-Type: application/json" https://www.googleapis.com/qpxExpress/v1/trips/search?key=mykeyhere
headers = {
    'Content-Type': 'application/json',
}
params = (
    ('key', 'mykeyhere'),
)
data = open('request.json')
response = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search',
                         headers=headers, params=params, data=data)

"""
Eğer data içinde değişiken kullanmak isterseniz.
data = {"url": url}
            response = requests.post('http://127.0.0.1:1337/', headers=headers,
                                     data=json.dumps(data))
"""


# GET isteğinin yapılması
r = requests.get('https://github.com/timeline.json')
r.json()


r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.status_code)
# 200
print(r.headers['content-type'])
# 'application/json; charset=utf8'
print(r.encoding)
# 'utf-8'
print(r.text)
# u'{"type":"User"...'
print(r.json())
# {u'private_gists': 419, u'total_private_repos': 77, ...}
