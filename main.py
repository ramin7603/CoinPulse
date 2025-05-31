import os
import requests
import json
from datetime import datetime

SYMBOLS = {
    'bitcoin': 'BTC',
    'ethereum': 'ETH',
    'dogecoin': 'DOGE',
    'cardano': 'ADA',
    'ripple': 'XRP',
    'litecoin': 'LTC',
    'polkadot': 'DOT'
}


# $ https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd


def fetch_crypto_prices(cryptos):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ','.join(cryptos),
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("خطا در دریافت داده‌ها:", response.status_code)
        return {}


def save_for_frontend(data, filename="crypto_table_data.json"):
    today_str = datetime.now().strftime('%Y-%m-%d')

    rows = []
    for crypto, prices in data.items():
        row = {
            "name": crypto.capitalize(),
            "symbol": SYMBOLS.get(crypto, crypto[:3].upper()),
            "price_usd": prices.get('usd', None),
            "last_updated": datetime.now().isoformat()
        }
        rows.append(row)

    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            all_data = json.load(f)
    else:
        all_data = {}

    all_data[today_str] = rows

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)

    print(f"Data for {today_str} saved to file '{filename}' successfully.")


if __name__ == "__main__":
    cryptos = list(SYMBOLS.keys()) 
    prices = fetch_crypto_prices(cryptos)
    if prices:
        save_for_frontend(prices)
