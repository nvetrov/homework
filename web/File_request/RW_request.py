'''
Задачи 9

+ Реализовать две функции: write_to_file(data) и read_file_data().
Которые соотвественно: пишут данные в файл и читают данные из файла.

+ Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
(сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
выводить в консоль все пары заголовки, сохранять полученный json в файл на диск. Вывести на экран сохранённый json файл.

+ Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
При помощи регулярных выражений нужно получить все ссылки со страницы на другие.
Ответить себе на вопрос удобно ли так делать?



BorisRubin
https://github.com/BorisRubin/TCEH-Homeworks/tree/master/Homework9/Main
'''
import re
import requests
import json
import os


def write_to_file(file, data, mode='w'):
    print('Writing to {}\n'.format(file))
    with open(file, mode) as newfile:
        newfile.write(data)




def read_file_data(file):
    print('Reading from {}\n'.format(file))
    try:
        opened_file = open(file)
        data = opened_file.read()
    finally:
        opened_file.close()

    return data


def read_file_json(file_json):
  try:
    with open(file_json) as f:
        data = json.load(f)
  finally:
     f.close()

  return data



def get_service_data(url):
    result = requests.get(url)

    if result.status_code == 200:
        return result
    else:
        raise RuntimeError("Request from url = '{}' ended with code {}".format(url, result.status_code))


# ОСНОВАЯ ФУНКЦИЯ МОДУЛЯ
def main():
    print('***** TASK 9 part 1 *****\n')
    textdata = 'Hello, this is the example of the data!\nThis is the last line of this text\n'
    print('\nDATA TO SAVE IN FILE:',textdata)
    write_to_file('some_data.txt', textdata)
    print(read_file_data('some_data.txt'))

    print('\n***** TASK 9 part 2 *****\n')
    response = get_service_data('https://jsonplaceholder.typicode.com/comments/')
    json_data = response.json()
    print('\nJSON response saved in file \'site_response.json\'')
    with open('data.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii=False, sort_keys=False)
    result_json = read_file_json('data.json')


    print(result_json[0])

    # for i in result_json:
    #   print([i])








if __name__ == '__main__':
    main()
