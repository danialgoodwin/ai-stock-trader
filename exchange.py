

def check():
    print('check()')


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


if __name__ == '__main__':
    main()
