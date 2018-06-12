import json
from IOpy import way_batter

if __name__ == "__main__":
    data = way_batter('data.json')
    print('raw data is', data, type(data))
    print('------------------------------')

    # from string to object
    obj = json.loads(data)
    print(obj, type(obj))

    print(obj['name'], obj['age'])
    print(obj['cars'])
    print()

    # print('dumping object to text:')
    # obj['new-value'] = 'secret'
