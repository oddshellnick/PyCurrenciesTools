class ExchangeRateNotFoundError(Exception):
    """
    Exception raised when an exchange rate is not found.
    """

    def __init__(self, from_currency: str, to_currency: str):
        """
        Initializes the exception with the given error message.

        Args:
            from_currency (str): The abbreviation of the currency to be exchanged.
            to_currency (str): The abbreviation of the currency to be converted to.
        """
        super().__init__(f'Exchange rate from "{from_currency}" to "{to_currency}" not found.')


class CurrencyTagNotFoundError(Exception):
    """
    Exception raised when a currency abbreviation is not found.
    """

    def __init__(self, tag: str):
        """
        Initializes the exception with the given error message.

        Args:
            tag (str): The error message.
        """
        super().__init__(f'Tag "{tag}" not found.')
