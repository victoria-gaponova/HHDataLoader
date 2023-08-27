from pycbrf import ExchangeRates
from datetime import datetime
from decimal import Decimal


def get_currency_converter(currency: str) -> Decimal:
    """ Конвертирует валюту в российские рубли

    :param currency: валюта
    :return: российские рубли
    """
    # получаем текущую дату
    current_date = datetime.now().strftime('%Y-%m-%d')
    # создадим словарь с текущими валютами
    rates = ExchangeRates(current_date)
    currency = _check_currency(currency)
    current_data = list(filter(lambda el: el.code == currency, rates.rates))[0].rate
    return Decimal(current_data)


def _check_currency(currency: str) -> str:
    """
    Проверяет правильность обозначения белорусского рубля и исправляет при необходимости.
    :param currency:
    :return: валюту
    """
    if currency == 'BYR':
        return 'BYN'
    else:
        return currency
