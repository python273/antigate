# -*- coding: utf-8 -*-
import requests as http  # http://docs.python-requests.org/en/latest/
import time


class Antigate():
    """ """
    def __init__(self, key, params={}):
        self.key = key  # Ключ antigate
        self.params = params

    def capcha(self, path):
        """ Send capcha
            -path - path to capcha
        """
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

        text = self.check(capcha_id)

        return Capcha(text, capcha_id, self.key)

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
        """ Check the balance of Antigate"""
        data = {
            'action': 'getbalance',
            'key': self.key
        }

        response = http.post('http://antigate.com/res.php', data).text

        if not 'ERROR' in response:
            return float(response)
        else:
            raise antigate_error(response)


class Capcha():
    """ Capcha class """
    def __init__(self, text, capcha_id, key):
        self.text = text
        self.capcha_id = capcha_id
        self.key = key

    def __str__(self):
        return self.text

    def __unicode__(self):
        return unicode(self.text)

    def __repr__(self):
        return self.text

    def bad(self):
        """ Report bad capcha """
        data = {
            'action': 'reportbad',
            'key': self.key,
            'id': self.capcha_id
        }

        response = http.post('http://antigate.com/res.php', data).text

        if 'OK' in response:
            return True
        else:
            raise antigate_error(response)


class antigate_error(Exception):
    pass

if __name__ == '__main__':
    print help(Antigate)
    print help(Capcha)
