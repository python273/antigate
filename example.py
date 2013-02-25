# -*- coding: utf-8 -*-
import antigate


def main():
    antigate_key = '0342c459325c4b452c50811c7df8e8c6'

    a = antigate.Antigate(antigate_key)
    a.params = {'max_bid': '0.001'}

    print 'Balance: %s' % (a.balance())
    capcha = a.capcha('./example_capcha.jpeg')
    print capcha

if __name__ == '__main__':
    main()
