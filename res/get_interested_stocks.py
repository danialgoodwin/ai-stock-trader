from pathlib import Path




def get_file():
    INTERESTED_STOCKS_FILE = 'interested-stocks.txt'
    if Path(INTERESTED_STOCKS_FILE).is_file():
        return INTERESTED_STOCKS_FILE
    return f'res/{INTERESTED_STOCKS_FILE}'


def get_interested_stocks() -> []:
    print(f'get_interested_stocks()')
    with Path(get_file()).open('r') as f:
        stocks = []
        for line in f.readlines():
            line = line.rstrip('\n')
            if line.startswith('#'): continue
            if line == '': continue
            stocks.append(line)
        return stocks


def main():
    print('main()')
    stocks = get_interested_stocks()
    print(f'stocks={stocks}')


if __name__ == '__main__':
    main()
