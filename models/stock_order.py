# Resources:
# - https://www.ally.com/api/invest/documentation/trading/


class StockOrder:
    def __init__(self, account, symbol, quantity, order_type='market'):
        print('__init__')
        self.account = account
        self.symbol = symbol
        self.quantity = quantity
        self.order_type = order_type

    def _get_order_type_id(self):
        return {
            'market': 1,
            'limit': 2,
            'stopMarket': 3,
            'stopLimit': 4
        }.get(self.order_type, 0)

    def get_fixml(self):
        print('get_fixml')
        return f'''
            <FIXML xmlns="http://www.fixprotocol.org/FIXML-5-0-SP2">
                <Order TmInForce="0" Typ="1" Side="1" Acct="${self.account}">
                    <Instrmt SecTyp="CS" Sym="${self.symbol}"/>
                    <OrdQty Qty="${self.quantity}"/>
                </Order>
            </FIXML>'''
