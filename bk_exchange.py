from dataclasses import dataclass


class BkExchange:
    def __init__(self):
        pass

    def place_order(self, account, bs, symbol, amount, price):
        pass

    def amend_order_with_oid(self, oid, **kwargs):
        pass

    def cancel_order_with_oid(self, oid):
        pass

    def list_orders(self, account):
        pass

    def query_order_with_oid(self, oid):
        pass
