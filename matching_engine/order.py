import numpy as np
import uuid
import time


class Order:
    def __init__(
        self,
        security_id: str,
        trader_id: str,
        price: np.float64,
        quantity: np.int32,
        order_type: str,
    ) -> None:
        self.security_id: str = security_id
        self.trader_id: str = trader_id
        self.order_id: uuid.UUID = uuid.uuid4()
        self.price: np.float64 = price
        self.quantity: np.int32 = quantity
        self.order_type: str = order_type  # either 'buy' or 'sell'
        self.timestamp: time.struct_time = time.time()

    def __str__(self) -> str:
        return f"Submitted {self.order_type} for {self.security_id} at ${self.price} for a quantity of {self.quantity} at {self.timestamp}"

    def __repr__(self) -> str:
        return f"<<<|{self.timestamp}|{self.security_id}|{self.price}|{self.quantity}|{self.order_type}|{self.trader_id}|>>>"
