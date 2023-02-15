# Define the Order class to represent orders in the order book.
import uuid
import numpy as np
import time
from order import Order


class OrderBook:
    def __init__(
        self,
    ) -> None:
        self.buy_orders: dict = {}  # This should be a proper database
        self.sell_orders: dict = {}  # This should be a proper database
        self.orders: dict = {}

    def add_order(self, order: Order):
        if order.order_type == "buy":
            if order.price in self.buy_orders:
                # Check if price in buy orders and then append the new order
                # Implement FIFO later for priorities in matching engine
                # Potentially add to a dict of timestamps too within the price level
                self.buy_orders[order.price].append(order)

                self.buy_orders[order.price].sort(key=lambda x: (x.price, x.timestamp))

            else:  # Presumebly order price level not in price book so add it
                self.buy_orders[order.price] = [order]
            self.orders[order.order_id] = order

        if order.order_type == "sell":
            if order.price in self.sell_orders:

                self.sell_orders[order.price].append(order)

                self.sell_orders[order.price].sort(key=lambda x: (x.price, x.timestamp))

            else:
                self.sell_orders[order.price] = [order]

            self.sell_orders[order.order_id] = order

    def remove_order(self, order: Order):
        if order.order_type == "sell":
            if order.price in self.sell_orders:
                self.sell_orders[order.price].remove(order)
                # add check here if any more orders in the same price level: if not delete that price level
                if not self.sell_orders[order.price]:
                    del self.sell_orders[order.price]
        else:
            if order.price in self.buy_orders:
                self.buy_orders[order.price].remove(order)
                if not self.buy_orders[order.price]:
                    del self.buy_orders[order.price]

        del self.orders[order.order_id]

    def update_order(self, order: Order):
        # first check if order_id exists
        try:
            self.orders[order.order_id]
        except:
            raise ValueError(
                f"Order ID {order.order_id} doesn't exist in the orderbook"
            )
        # Todo()! implement logic

    def __str__(self) -> str:
        return f"Buy Orders{str(self.buy_orders)} - Sell Orders{str(self.sell_orders)}"


if __name__ == "__main__":
    buy_order = Order("AAPL", 1, 123.3, 4, "buy")
    oBook = OrderBook()
    oBook.add_order(buy_order)
    buy_order = Order("AAPL", 1, 123.3, 4, "buy")

    oBook.add_order(buy_order)
    buy_order = Order("AAPL", 1, 123.2, 4, "buy")
    oBook.add_order(buy_order)

    oBook.remove_order(buy_order)

    oBook.update_order(buy_order)

    print(oBook.orders)
    print(oBook)
