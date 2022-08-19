from pycbrf import ExchangeRates
from datetime import date, timedelta


#вызов функции:
# value_function(value)

class ValueCourse:
    value = {}

    today = str(date.today())#дата:сегодня
    yesterday = str(date.today() - timedelta(days=1))#дата:вчера
    one_day_ago = str(date.today() - timedelta(days=2))#дата:

    class TODAY:#данные за сегоня
        def __init__(self, today):
            rates = ExchangeRates(today)
            self.USD = str(rates['USD'].value)
            self.EUR = str(rates['EUR'].value)
            self.CNY = str(rates['CNY'].value)

    class YESTRDAY:#данные за вчера
        def __init__(self, yesterday):
            rates = ExchangeRates(yesterday)
            self.USD = str(rates['USD'].value)
            self.EUR = str(rates['EUR'].value)
            self.CNY = str(rates['CNY'].value)

    class ONE_DAY_AGO:#данные за позавчера
        def __init__(self, one_day_ago):
            rates = ExchangeRates(one_day_ago)
            self.USD = str(rates['USD'].value)
            self.EUR = str(rates['EUR'].value)
            self.CNY = str(rates['CNY'].value)


    value_today = TODAY(today)#экзепляр объекта 

    value_yestrday = YESTRDAY(yesterday)#экземпляр объекта вчера

    value_one_day_ago = ONE_DAY_AGO(one_day_ago)#экземпляр объекта позавчера

    value['usd'] = {today: value_today.USD, yesterday: value_yestrday.USD}# , {one_day_ago: value_one_day_ago.USD}#добавление значений 'сегоня' в словарь

    value['eur'] = {today: value_today.EUR, yesterday: value_yestrday.EUR}# , {one_day_ago: value_one_day_ago.EUR}#добавление значений 'вчера' в словарь

    value['cny'] = {today: value_today.CNY, yesterday: value_yestrday.CNY}# , {one_day_ago: value_one_day_ago.CNY}#добавление значений 'позавчера' в словарь

# print(ValueCourse().value['usd']['2022-07-26'])