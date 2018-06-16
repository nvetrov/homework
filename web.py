# from requests import get
import requests

__author__ = 'vetrov nikolay'
'''
with open('dataset_3378_2 (1).txt', 'r') as inf:
    x = requests.get(inf.readline().strip())
    print((x.text))

url = 'https://api.github.com/user'

r = requests.get(url, auth=('nvetrov@gmail.com', 'C1vmdpalc33'))
cookies = {'cookies_are':'working'}
print(r.status_code) # 200 все хорошо.
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print('--------')
print(r.content)
print('--------')
r = requests.get(url,cookies=cookies)
print(r.cookies)
'''


def get_url():
    r = requests.get('http://petstore.swagger.io/v2/pet/1')
    print('r.status_code->', r.status_code)  # 200 все хорошо.
    print("r.headers['content-type']->", r.headers['content-type'])
    print('r.encoding->', r.encoding)
    print("r.text ->", r.text)




if __name__ == '__main__':
    get_url()
