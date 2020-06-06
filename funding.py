import orjson
import requests

'''
Bybit/Binance/Okex(CST): 3AM, 11AM, 7PM
Bybit/Binance/Okex(24hr-CST): 3, 11, 19 

Bitmex/Huboi(CST): 7AM, 3PM, 11PM
Bitmex/Huboi(24hr-CST): 7, 15, 23
'''

def bitmex_funding():
    url_usd = r"https://www.bitmex.com/api/v1/funding?symbol=xbt%3Aperpetual&count=1&reverse=true"
    resp_usd = orjson.loads(requests.get(url_usd).text)
    return resp_usd[0]["fundingRate"]

def okex_funding():
    url_usd = r"https://www.okex.com/api/swap/v3/instruments/BTC-USD-SWAP/funding_time"
    url_usdt = r"https://www.okex.com/api/swap/v3/instruments/BTC-USDT-SWAP/funding_time"
    resp_usd = orjson.loads(requests.get(url_usd).text)
    resp_usdt = orjson.loads(requests.get(url_usdt).text)
    return(resp_usd["funding_rate"], resp_usd["estimated_rate"],
           resp_usdt["funding_rate"], resp_usdt["estimated_rate"] )

def binance_funding():
    url_usdt = r"https://fapi.binance.com/fapi/v1/fundingRate?limit=1&symbol=BTCUSDT"
    resp_usdt = orjson.loads(requests.get(url_usdt).text)
    return resp_usdt[0]["fundingRate"]

def bybit_funding():
    url_usdt = r"https://api.bybit.com/public/linear/funding/prev-funding-rate?symbol=BTCUSDT"
    resp_usdt = orjson.loads(requests.get(url_usdt).text)
    return resp_usdt["result"]["funding_rate"]

def huboi_funding():
    url_usd = r"https://api.btcgateway.pro/swap-api/v1/swap_funding_rate?&contract_code=BTC-USD"
    resp_usd = orjson.loads(requests.get(url_usd).text)
    return (resp_usd["data"]["funding_rate"], resp_usd["data"]["estimated_rate"])

def get_ratio():
    url = r"https://api-pub.bitfinex.com/v2/ticker/tUSTUSD"
    resp = orjson.loads(requests.get(url).text)
    return resp[6]

def round_one_info_notif():
    info = {
        "bybit-usdt" : bybit_funding,
        "last-binace-usdt": binance_funding,
        "okex-usd-estimate": okex_funding()[1],
        "okex-usdt-estimate": okex_funding()[3],
        "current USD/USDT": get_ratio()
    }
    return info

def round_two_info_notif():
    info = {
        "bitmex" : bitmex_funding(),
        "huboi-usd-estimated": huboi_funding()[1],
        "current USD/USDT": get_ratio()
    }
    return info

def round_one_info():
    info = {
        "bybit": bybit_funding(),
        "last-binance-usdt": binance_funding(),
        "okex-usd": okex_funding()[0],
        "okex-usdt" : okex_funding()[1],
        "current USD/USDT": get_ratio()
    }
    return info

def round_two_info():
    info = {
        "bitmex": bitmex_funding(),
        "huboi-usd": huboi_funding()[0],
        "current USD/USDT": get_ratio()
    }
    return info


