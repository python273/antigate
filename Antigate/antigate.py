# -*- coding: utf-8 -*-
import requests as http  # http://docs.python-requests.org/en/latest/
import time


class Antigate():
    def __init__(self, key, params={}):
        self.key = key  # Ключ antigate
        self.params = params

    def capcha(self, path):
        """ Отправить капчу. В path путь до картинки с капчей """
        data = {
            'method': 'post',
            'key': self.key
            }
        data.update(self.params)
        files = {'file': open(path, 'rb')}

        response = http.post('http://antigate.com/in.php', data, files=files).text

        if 'OK' in response:
            capcha_id = response.split('|')[1]
        else:
            raise antigate_error(response)

        response = self.check(capcha_id)

        return {'id': capcha_id, 'text': response}

    def check(self, capcha_id):
        data = {
            'action': 'get',
            'key': self.key,
            'id': capcha_id
            }

        while True:
            time.sleep(5)
            response = http.post('http://antigate.com/res.php', data).text

            if 'OK' in response:
                return response.split('|')[1]

            elif 'ERROR' in response:
                raise antigate_error(response)

    def balance(self):
        """ Проверить баланс antigate"""
        data = {
            'action': 'getbalance',
            'key': self.key
            }

        response = http.post('http://antigate.com/res.php', data).text

        if not 'ERROR' in response:
            return float(response)
        else:
            raise antigate_error(response)

    def bad(self, capcha_id):
        """ Сообщить о неправильной капче """
        data = {
            'action': 'reportbad',
            'key': self.key,
            'id': capcha_id
            }

        response = http.post('http://antigate.com/res.php', data).text

        if 'OK' in response:
            return True
        else:
            raise antigate_error(response)


class antigate_error(Exception):
    pass
