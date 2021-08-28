import datetime

import yfinance as yf
import logging
from pathlib import Path

from res.get_interested_stocks import  get_interested_stocks


OUTPUT_DIRECTORY = 'price-history'

logging.basicConfig(level=logging.DEBUG)


def save(stock_price_history):
    print('save()')


def get_stock_price_history(stock_ticker: str):
    print(f'get_stock_price_history({stock_ticker})')
    ticker = yf.Ticker(stock_ticker)
    logging.debug(f'ticker={ticker}')
    history = ticker.history(period='max', actions=False)
    logging.debug(f'history={history}')
    return history


def is_price_history_file_exists(stock_ticker) -> bool:
    files = Path(OUTPUT_DIRECTORY).glob('*')
    for file in files:
        if file.name.startswith(stock_ticker): return True
    return False


def main():
    print('main()')
    Path(OUTPUT_DIRECTORY).mkdir(parents=True, exist_ok=True)
    for stock_ticker in get_interested_stocks():
        if is_price_history_file_exists(stock_ticker):
            print(f'Price history already exists for {stock_ticker}')
            continue

        history = get_stock_price_history(stock_ticker)
        logging.debug(f'history.keys()={history.keys()}')
        output_contents = []
        for h in zip(history.index, history['Close']):
            logging.debug(f'h={h}')
            output_contents.append(f'{h[0].isoformat()[0:10]} {h[1]}\n')

        start_date = output_contents[0].split()[0]
        stop_date = output_contents[-1].split()[0]

        output_file = Path(f'{OUTPUT_DIRECTORY}/{stock_ticker}--history--{start_date}-to-{stop_date}.txt')
        with output_file.open('w+') as f:
            f.write(''.join(output_contents))


if __name__ == '__main__':
    main()
