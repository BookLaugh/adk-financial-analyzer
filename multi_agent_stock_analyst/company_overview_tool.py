# -*- coding: utf-8 -*-
import os

import requests
from google.adk.tools import FunctionTool


def get_company_overview(symbol: str) -> dict[str, str]:
    """
    Retrieves company's current financial data from the AlphaVantage.co API

    Args:
       symbol: Ticker of the company, the stock market symbol, e.g. AMZN, GOOG, META

    Returns:
        Dict with keys like MarketCapitalization, EBITDA, PERatio, PEGRatio, BookValue, EPS, ProfitMargin, OperatingMarginTTM, TrailingPE, ForwardPE.
        All values are strings, but can contain numbers or dates. Dates are formatted YYYY-MM-DD, e.g. 2024-12-31

    """
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
    if not api_key:
        raise ValueError("API AlphaVantage key is missing. Set the env value ALPHAVANTAGE_API_KEY.")

    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Throws an error for statuses 4xx/5xx
        data = response.json()
        if not data:
            print(f"No data for {symbol}")
        if "ErrorMessage" in data or "Information" in data:
            print(f"AlphaVantage error or limit reached: {data}")
        keys_to_drop = ['Name', 'AssetType', 'Description', 'Industry', 'Address', 'OfficialSite', 'FiscalYearEnd', 'CIK',
                        'Exchange', 'Country']
        for key in keys_to_drop:
            data.pop(key, '')

        return data
    except requests.exceptions.RequestException as e:
        print(f"Error when retrieving data from AlphaVantage: {e}")
    except ValueError as e:
        print(f"Failed to parse json from AlphaVantage: {e}")
    return {}


company_overview_tool = FunctionTool(func=get_company_overview)

if __name__ == "__main__":
    # Usage example:
    stock_symbol = "META"
    overview = get_company_overview(stock_symbol)
    if overview:
        print(f"Overview value for {stock_symbol}:")
        print(overview)
