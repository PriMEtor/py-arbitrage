# coding: utf-8
# Created by lei at 2022/5/6 00:03
from binance.error import ParameterArgumentError
from binance.lib.utils import (
    check_required_parameter,
    check_type_parameter,
    convert_list_to_json_array,
)
from binance.lib.utils import check_required_parameters


def ping(self):
    """Test Connectivity
    Test connectivity to the Rest API.

    GET /fapi/v1/ping

    https://binance-docs.github.io/apidocs/futures/en/#test-connectivity

    """

    url_path = "/fapi/v1/ping"
    return self.query(url_path)


def time(self):
    url_path = "/fapi/v1/time"
    return self.query(url_path)


def exchange_info(self):

    url_path = "/fapi/v1/exchangeInfo"
    return self.query(url_path)


def depth(self, symbol: str, **kwargs):
    """Get orderbook.

    GET /api/v3/depth

    https://binance-docs.github.io/apidocs/spot/en/#order-book

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 100; valid limits:[5, 10, 20, 50, 100, 500, 1000, 5000]
    """

    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/depth", params)


def trades(self, symbol: str, **kwargs):
    """Recent Trades List
    Get recent trades (up to last 500).

    GET /api/v3/trades

    https://binance-docs.github.io/apidocs/spot/en/#recent-trades-list

    Args:
        symbol (str): the trading pair
    Keyword Args:
        limit (int, optional): limit the results. Default 500; max 1000.
    """
    check_required_parameter(symbol, "symbol")
    params = {"symbol": symbol, **kwargs}
    return self.query("/fapi/v1/trades", params)

