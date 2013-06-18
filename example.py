# -*- coding: utf-8 -*-
import pyantigate


def main():
    antigate_key = '23eeeb4347bdd26bfc6b7ee9a3b755dd'

    a = pyantigate.Antigate(antigate_key)
    a.params = {'max_bid': '0.001'}

    print('Balance: %s' % a.balance())

    capcha = a.capcha('./example_capcha.jpeg')
    print('Capcha text: %s' % capcha)

    if capcha.text.lower() != 'zz2xq':  # for example_capcha.jpeg
        capcha.bad()  # Report bad capcha code
        print('Report bad')


if __name__ == '__main__':
    main()
