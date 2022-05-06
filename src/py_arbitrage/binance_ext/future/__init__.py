# coding: utf-8
# Created by lei at 2022/5/5 23:54
from binance.api import API


class Future(API):

    def __init__(self, key=None, secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://fapi.binance.com"
        super().__init__(key, secret, **kwargs)

    # MARKETS
    from .market import ping
    from .market import time
    from .market import exchange_info
    from .market import depth
    from .market import trades



