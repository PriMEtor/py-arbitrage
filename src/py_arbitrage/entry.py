# coding: utf-8
# Created by lei at 2022/4/20 22:22
from binance.spot import Spot


def main():
    client = Spot()
    # Get server timestamp
    print(client.time())
    # Get klines of BTCUSDT at 1m interval
    print(client.klines("BTCUSDT", "1m"))
    # Get last 10 klines of BNBUSDT at 1h interval
    print(client.klines("BNBUSDT", "1h", limit=10))


if __name__ == '__main__':
    main()
