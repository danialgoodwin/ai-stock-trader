import json

from requests_oauthlib import OAuth1Session


BASE_API = 'https://api.tradeking.com/v1'
BASE_STREAM_API = 'https://stream.tradeking.com/v1'


AUTH_SESSION = OAuth1Session('y018AUt7iwf7oU9PT71jmzB6aGwhYDHvaOK9FyFZVgQ3',
                            client_secret='bbFshnoBVPsLtYr7mcq04qb2SS2gFRO5WYVyDmJ7A3s7',
                            resource_owner_key='6LD9pELOGa6eXiFr0kQKKesrQHNMiay6vSvqu3kJqUQ2',
                            resource_owner_secret='qtuiivJjKRRI2H1jeaiSmzL0YIUfAGUr29C67uKVUeQ4')


def check():
    print('check()')


def _wrap_fixml(xml : str) -> str:
    return f'<FIXML xmlns="http://www.fixprotocol.org/FIXML-5-0-SP2">{xml}</FIXML>'


def get_price(stock_symbol='ROKU', date=None):
    print(f'get_price({stock_symbol})')
    response = AUTH_SESSION.get(f'{BASE_API}/market/ext/quotes.json?symbols={stock_symbol}').json()
    # response = AUTH_SESSION.get(f'{BASE_STREAM_API}/market/quotes.json?symbols={stock_symbol}').json()

    print(f'response={json.dumps(response, indent=4)}')
    quote = response['response']['quotes']['quote']
    return {
        'currentPrice': quote['last'],
        'currentDate': quote['date'],
        'previousClosePrice': quote['pcls'],
        'previousCloseDate': quote['pr_date']
    }


def buy(account='12345678', stock_symbol='ROKU', number_of_stocks=1):
    print('buy()')
    fixml = _wrap_fixml(f'''
            <Order TmInForce="0" Typ="1" Side="1" Acct="${account}">
                <Instrmt SecTyp="CS" Sym="${stock_symbol}"/>
                <OrdQty Qty="${number_of_stocks}"/>
            </Order>''')


def sellAtMarket(account='12345678', stock_symbol='ROKU', number_of_stocks=1):
    print('sell()')
    fixml = _wrap_fixml(f'''
            <Order TmInForce="0" Typ="1" Side="2" Acct="${account}">
                <Instrmt SecTyp="CS" Sym="${stock_symbol}"/>
                <OrdQty Qty="${number_of_stocks}"/>
            </Order>''')


def sellAtLimit(account='12345678', stock_symbol='ROKU', number_of_stocks=1, price='15'):
    print('sell()')
    fixml = _wrap_fixml(f'''
            <Order TmInForce="0" Typ="2" Side="1" Px="${price}" Acct="${account}">
                <Instrmt SecTyp="CS" Sym="${stock_symbol}"/>
                <OrdQty Qty="${number_of_stocks}"/>
            </Order>''')


def sellAtStop(account='12345678', stock_symbol='ROKU', number_of_stocks=1):
    print('sell()')
    fixml = _wrap_fixml(f'''
            <Order TmInForce="0" Typ="1" Side="2" Acct="${account}">
                <Instrmt SecTyp="CS" Sym="${stock_symbol}"/>
                <OrdQty Qty="${number_of_stocks}"/>
            </Order>''')


def main():
    print('main()')
    price = get_price('ROKU')
    print(f'ROKU={price}')


if __name__ == '__main__':
    main()
