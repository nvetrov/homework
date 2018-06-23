# Реализовать следующую логику:
# получать при помощи requests данные сервиса
# https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую,
# например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки,
# сохранять полученный json в файл на диск

import requests
import json

# def mywrite_to_file(filename: str, data: list):
#     print('Write to file {}'.format(filename))
#     with open(filename, "w") as file:
#         file.writelines(data)
#
#
# def read_file_data(filename):
#     with open(filename, "r") as file:
#         data = file.read()
#         return data
#


def print_headers_and_save_json(url: str, filename):
    r = requests.get(url)

    headers_dict = dict(r.headers)
    for key, value in headers_dict.items():
        print(key+':', value)

    with open(filename, 'wb') as file:
        for chunk in r.iter_content(chunk_size=128):
            file.write(chunk)




                            # 'jsonplaceholdercomments.json')

if __name__ == '__main__':
  print_headers_and_save_json('https://jsonplaceholder.typicode.com/comments', 'data.json')

