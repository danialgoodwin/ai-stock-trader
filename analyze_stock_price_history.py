import logging
import statistics

from datetime import date
from pathlib import Path


NUMBER_OF_DATA_POINTS_FOR_NELSON_RULES = 12  # Arbitrary
PRICE_HISTORY_DIRECTORY = 'price-history'
ANALYZE_DIRECTORY = 'out/analyze'


logging.basicConfig(level=logging.DEBUG)


def percent_change(old_price, new_price, round=3):
    if old_price == 0: return 0
    return (new_price - old_price) / old_price


def analyze_stock_price_history(stock_ticker, history, dates, prices):
    print(f'analyze_stock_price_history({stock_ticker})')
    if type(history) is str:
        pass
    print(f'    Initial price: {history[0]}')
    print(f'    Latest price: {history[-1]}')

    max_gain = 0
    max_loss = 0
    max_gain_i = 0
    max_loss_i = 0
    for i in range(len(prices) - 1):
        p_change = percent_change(prices[i], prices[i + 1])
        if p_change > max_gain:
            max_gain = p_change
            max_gain_i = i + 1
        elif p_change < max_loss:
            max_loss = p_change
            max_loss_i = i + 1

    print(f'    Biggest one-day gain: {max_gain:.4f} on {dates[max_gain_i]}')
    print(f'    Biggest one-day loss: {max_loss:.4f} on {dates[max_loss_i]}')

    print(f'    Mean: ')
    print(f'    Standard deviation: ')

    print(f'    ----------')

    print(f'    5-year change:  {percent_change(prices[-1256], prices[-1]):.4f}  ({dates[-1256]})')
    print(f'    4-year change:  {percent_change(prices[-1004], prices[-1]):.4f}  ({dates[-1004]})')
    print(f'    3-year change:  {percent_change(prices[-753],  prices[-1]):.4f}  ({dates[-753]})')
    print(f'    2-year change:  {percent_change(prices[-502],  prices[-1]):.4f}  ({dates[-502]})')
    print(f'    1-year change:  {percent_change(prices[-251],  prices[-1]):.4f}  ({dates[-251]})')
    print(f'    3-month change: {percent_change(prices[-66],   prices[-1]):.4f}  ({dates[-66]})')
    print(f'    1-month change: {percent_change(prices[-22],   prices[-1]):.4f}  ({dates[-22]})')
    print(f'    7-day change:   {percent_change(prices[-7],    prices[-1]):.4f}')
    print(f'    2-day change:   {percent_change(prices[-3],    prices[-1]):.4f}')
    print(f'    1-day change:   {percent_change(prices[-2],    prices[-1]):.4f}')
    print('\n')


def main():
    print('main()')
    for file in Path(PRICE_HISTORY_DIRECTORY).glob('*'):
        stock_ticker = file.name.split('--')[0]
        with Path(file).open('r') as f:
            data = []
            dates = []
            prices = []
            for line in f.readlines():
                split = line.split()
                dates.append(date.fromisoformat(split[0]))
                prices.append(float(split[1]))
                data.append({
                    'date': date.fromisoformat(split[0]),
                    'price': float(split[1])
                })
            try:
                analyze_stock_price_history(stock_ticker, data, dates, prices)
            except Exception as e:
                logging.error(f'Error with {stock_ticker}: {e}')


if __name__ == '__main__':
    main()
