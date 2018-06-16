import json
from IOpy import way_batter

if __name__ == "__main__":
    data = way_batter('data.json')
    # data = way_batter('response.json')
    print('raw data is', data, type(data))
    print('------------------------------')

    # from string to object
    obj = json.loads(data)
    # print(obj, type(obj))
    # print(obj['category'], obj['name'])
    #
    print(obj['name'], obj['age'])
    print(obj['cars'])
    print()
    # From object to text
    print('dumping object to text:')
    obj['news-value'] = 'secret3'
    print(json.dumps(obj, sort_keys=True, indent=5))
