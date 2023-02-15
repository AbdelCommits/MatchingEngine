from orderBook import OrderBook


class MatchingEngine:
    def __init__(self, order_book: OrderBook) -> None:
        self.order_book = order_book

    def match_orders(self, order):
        pass
