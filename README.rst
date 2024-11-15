PyCurrenciesTools: A Python library for easy currency conversion and information retrieval.
===========================================================================================

This library provides a simple and efficient way to work with currencies, including getting exchange rates and converting amounts between different currencies.  It leverages live exchange rate data for up-to-date conversions.


Key Features
------------

* **Real-time Exchange Rates:** Fetch the latest exchange rates between various currencies using `get_exchange_rate()`.
* **Currency Conversion:** Easily convert amounts from one currency to another with `exchange_currency()`.
* **Currency Symbols and Tags:** Access a comprehensive list of currency abbreviations (tags) and symbols using the `PyCurrenciesTools.data.CurrenciesTags` and `PyCurrenciesTools.data.CurrenciesSymbols` classes.
* **Error Handling:** Clear error messages are raised for invalid currency tags or unavailable exchange rates, simplifying debugging.


Installation
------------

Install PyCurrenciesTools using pip:

.. code-block:: bash

    pip install PyCurrenciesTools


Usage Examples
--------------

**Getting the exchange rate:**

.. code-block:: python

    from PyCurrenciesTools import get_exchange_rate

    try:
        rate = get_exchange_rate("USD", "EUR")
        print(f"The exchange rate from USD to EUR is: {rate}")
    except Exception as e:
        print(f"Error: {e}")


**Converting currency:**

.. code-block:: python

    from PyCurrenciesTools import exchange_currency

    try:
        converted_amount = exchange_currency(100, "USD", "EUR")
        print(f"100 USD is equal to {converted_amount} EUR")
    except Exception as e:
        print(f"Error: {e}")


**Accessing Currency Symbols and Tags:**

.. code-block:: python

    from PyCurrenciesTools.data import CurrenciesTags, CurrenciesSymbols

    usd_tag = CurrenciesTags.united_states_dollar
    usd_symbol = CurrenciesSymbols.united_states_dollar

    print(f"USD Tag: {usd_tag}")
    print(f"USD Symbol: {usd_symbol}")


Future Notes
------------

PyCurrenciesTools is actively maintained and we are continually working to improve its functionality and data accuracy. Future development may include expanding the range of supported currencies, providing historical exchange rate data, and adding more advanced currency-related features. We welcome contributions and suggestions from the community. Feel free to report any issues or propose new features.
