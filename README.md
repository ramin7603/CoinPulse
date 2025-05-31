
# CoinPulse

A simple Python script to fetch daily cryptocurrency prices (Bitcoin, Ethereum, Dogecoin, and more) from the free CoinGecko API and save the data as JSON for frontend use or further analysis.

## Features

* Fetches up-to-date prices of popular cryptocurrencies in USD
* Saves price data with date keys in a JSON file
* Easily extendable to track more cryptocurrencies
* Uses a free public API (CoinGecko) with no API key required
* Simple and easy to understand Python code

## Installation

Make sure you have Python 3 and pip installed.

Install required package:

```bash
pip install requests
```

## Usage

Run the script:

```bash
python main.py
```

After running, a file named `crypto_table_data.json` will be created with price data stored by date.

## Data Format

The JSON file stores data with date keys (`YYYY-MM-DD`), each containing a list of cryptocurrencies with details like this:

```json
{
  "2025-05-31": [
    {
      "name": "Bitcoin",
      "symbol": "BTC",
      "price_usd": 30000,
      "last_updated": "2025-05-31T14:00:00"
    },
    {
      "name": "Ethereum",
      "symbol": "ETH",
      "price_usd": 2000,
      "last_updated": "2025-05-31T14:00:00"
    }
  ]
}
```

## Customization

* Add or remove cryptocurrencies in the `SYMBOLS` dictionary in the script
* Change the output JSON filename in the `save_for_frontend` function
* Schedule the script to run periodically using cron or other schedulers for automatic updates

## License

This project is licensed under the MIT License.


