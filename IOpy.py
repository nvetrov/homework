def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as f:
        f.write(content)



def way_batter(filename):
    # print('Читаем файл  way_batter')
    with open(filename) as f:
        return f.read()


def read_file(filename):
    print('Читаем файл read_file')
    try:
        f = open(filename)
        context = f.read()
    finally:
        # f.close()
        print('Не удалось открыть файл методом read_file')



if __name__ == '__main__':
    # reading
    # print(way_batter('HomeWorks.txt'))
    # print(read_file('HomeWorks.txt'))
    print(way_batter('NewFile.txt'))
    # write_to_file(filename='NewFile.txt', content='NewLine\n', mode='a') #adds
