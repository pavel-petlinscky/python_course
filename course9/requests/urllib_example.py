# -*- coding: utf-8 -*-

from urllib.request import urlopen, Request
from urllib.parse import urlencode



def get_habrahabr():
    response = urlopen('http://habrahabr.ru/')
    print(response.code)
    print(response.info())
    html = response.read()
    response.close()

    print(html)


def find_pet_by_status(status):
    url = 'http://petstore.swagger.io/v2/pet/findByStatus'
    query_args = {'status': status}
    data = urlencode(query_args)
    full_url = '{}?{}'.format(url, data)
    print(full_url)

    request = Request(full_url, headers={
        'Accept': 'application/json'
        #'Accept': 'application/xml'
    })
    response = urlopen(request)
    print(response.info())
    #print(response.read())
    data = response.read()
    import json
    pets = json.loads(data)
    print(pets)
    response.close()


if __name__ == '__main__':
    # get_habrahabr()

    find_pet_by_status('sold')
