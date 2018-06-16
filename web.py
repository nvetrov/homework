from requests import get

with open('dataset_3378_2 (1).txt', 'r') as inf:
    x = get(inf.readline().strip())
    print((x.text))

# import requests
# url = 'https://api.github.com/user'
#
# r = requests.get(url, auth=('nvetrov@gmail.com', 'C1vmdpalc33'))
# cookies = {'cookies_are':'working'}
# print(r.status_code) # 200 все хорошо.
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print('--------')
# print(r.content)
# print('--------')
# r = requests.get(url,cookies=cookies)
# print(r.cookies)
