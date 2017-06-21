from pybitx.api import BitX
from collections import namedtuple

Account = namedtuple('Account', 'account_id, asset, balance, reserved, unconfirmed')
Ticker = namedtuple('Ticker', 'ask, bid, last_trade, pair, rolling_24_hour_volume, timestamp')
Asks = namedtuple('Asks', 'price, volume')
Bids = namedtuple('Bids', 'price, volume')
Trades = namedtuple('Trades', 'is_buy, price, timestamp, volume')
Orders = namedtuple('Orders', 'base, btc, completed_timestamp, counter, creation_timestamp, expiration_timestamp, fee_base, fee_btc, fee_counter, fee_zar, limit_price, limit_volume, order_id, pair, state, type, zar ')

# Setup the luno API
def setup_api():
#   Log in to Luno, Settings, API codes, Generate new, Specify permitions, copy username and password code.
    user = '-----YOUR----USERNAME-----'
    password = '----YOUR----SECRET----'
    api = BitX(user, password)
    return api

# Get accounts and balances
def luno_accounts(api):
    balance = api.get_balance()
    accounts = [Account(**k) for k in balance['balance']]
    return accounts

# Get BTXZAR ticker
def get_Ticker(api):
    temp = api.get_ticker('auth')
    ticker = Ticker(**temp)
    return ticker

# Get order Book
def get_orderBook(api, limit):
    orders = api.get_order_book(limit, 'auth')
    asks = [Asks(**k) for k in orders['asks']]
    bids = [Bids(**k) for k in orders['bids']]
    timestamp = orders['timestamp']
    return [asks, bids, timestamp]

# Get latest trades
def get_trades(api, limit):
    trades_ = api.get_trades(limit, 'auth')
    return [Trades(**k) for k in trades_['trades']]

# Get orders
def get_orders(api):
    orders = api.get_orders()
    return [Orders(**k) for k in orders['orders']]

if __name__ == '__main__':
    api = setup_api()
    accounts = luno_accounts(api)
    ticker = get_Ticker(api)
    order_book = get_orderBook(api, 10)
    trades = get_trades(api, 10)
    orders = get_orders(api)