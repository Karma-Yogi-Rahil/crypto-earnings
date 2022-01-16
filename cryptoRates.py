from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange
#import matplotlib.pyplot as plt
from pprint import pprint



cc = ForeignExchange(key='4U99I0CPK76X6E5G')
# There is no metadata in this call



def crpto_rates(crypto_symbol):
    
    data, _ = cc.get_currency_exchange_rate(from_currency=crypto_symbol,to_currency='USD')
    elon_usd_rate = data['5. Exchange Rate']
    return(elon_usd_rate)


def inr_rates():
    data, _ = cc.get_currency_exchange_rate(from_currency='USD',to_currency='INR')
    inr_rate = data['5. Exchange Rate']
    return(inr_rate)
    

    


