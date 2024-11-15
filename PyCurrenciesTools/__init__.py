import re

import PyWebRequests as request_functions

import PyCurrenciesTools.data as data
import PyCurrenciesTools.errors as errors


def tag_to_symbol(tag: str) -> str:
    """
    Converts a currency abbreviation to its symbol.

    Args:
        tag (str): The currency abbreviation.

    Returns:
        str: The currency symbol if found, otherwise None.

    Raises:
        CurrencyTagNotFoundError: If the currency abbreviation is not found.

    :Usage:
        tag_to_symbol("USD")
        '$'

        tag_to_symbol("XXX")
        Traceback (most recent call last):
        ...
        PyCurrenciesTools.errors.CurrencyTagNotFoundError: Tag "XXX" not found.
    """
    if tag in data.CurrenciesTags.__dict__.values():
        for tag_attr, value in data.CurrenciesTags.__dict__.items():
            if value == tag:
                return getattr(data.CurrenciesSymbols, tag_attr)

    raise errors.CurrencyTagNotFoundError(tag)


def get_exchange_rate(from_currency_tag: str, to_currency_tag: str) -> float:
    """
    Gets the exchange rate between two currencies.

    Args:
        from_currency_tag (str): The abbreviation of the currency to be exchanged.
        to_currency_tag (str): The abbreviation of the currency to be converted to.

    Returns:
        float: The exchange rate.

    Raises:
        ExchangeRateNotFoundError: If the exchange rate is not found.
        CurrencyTagNotFoundError: If from_currency_tag or to_currency_tag is not found.

    :Usage:
        get_exchange_rate("USD", "EUR")
        0.91

        get_exchange_rate("XXX", "YYY")
        Traceback (most recent call last):
        ...
        PyCurrenciesTools.errors.ExchangeRateNotFoundError: Exchange rate for "XXX" to "YYY" not found.
    """
    if from_currency_tag not in data.CurrenciesTags.__dict__.values():
        raise errors.CurrencyTagNotFoundError(from_currency_tag)

    if to_currency_tag not in data.CurrenciesTags.__dict__.values():
        raise errors.CurrencyTagNotFoundError(to_currency_tag)

    exchange_rate_element = request_functions.find_web_element(
        request_functions.get_html(
            f"https://currencylive.com/exchange-rate/1000-{from_currency_tag.lower()}-to-{to_currency_tag.lower()}-exchange-rate-today/"
        ),
        '//div[@class="rate-info"]/p[@class="text-bold"]',
    )

    if exchange_rate_element is not None:
        found_exchange_rate = re.search(
            r"\d+\s+%s\s+=\s+(\d+(?:\.\d+)?)\s+%s" % (from_currency_tag.upper(), to_currency_tag.upper()),
            exchange_rate_element.text,
        )

        if found_exchange_rate is not None:
            return float(found_exchange_rate.group(1))

    raise errors.ExchangeRateNotFoundError(from_currency_tag, to_currency_tag)


def exchange_currency(currency_amount: float, from_currency_tag: str, to_currency_tag: str) -> float:
    """
    Exchanges an amount of one currency to another.

    Args:
        currency_amount (float): The amount of currency to be exchanged.
        from_currency_tag (str): The abbreviation of the currency being exchanged.
        to_currency_tag (str): The abbreviation of the currency to be converted to.

    Returns:
        float: The converted amount of currency.

    Raises:
        ExchangeRateNotFoundError: If the exchange rate is not found.
        CurrencyTagNotFoundError: If from_currency_tag or to_currency_tag is not found.

    :Usage:
        exchange_currency(100, "USD", "EUR")
        0.91

        exchange_currency(100, "XXX", "YYY")
        Traceback (most recent call last):
        ...
        PyCurrenciesTools.errors.ExchangeRateNotFoundError: Exchange rate for "XXX" to "YYY" not found.
    """
    return currency_amount * get_exchange_rate(from_currency_tag, to_currency_tag)
