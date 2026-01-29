from __future__ import annotations

class Order:
    def __init__(self, cart:list, customer:str) -> None:
        self._cart = list(cart)
        self._customer = customer
    def __add__(self, other:str) -> Order:
        new_cart = self._cart.copy()
        new_cart.append(other)
        return Order(new_cart, self._customer)
    def __radd__(self, other: str) -> Order:
        new_cart = self._cart.copy()
        new_cart.append(other)
        return Order(new_cart, self._customer)

order = Order(["banana", "apple"], "Amy")
#print(3.5 + " cm")
new_order = order + "mango"
#.          __add__(self, string)
print(new_order._cart)
new_order = "mango" + order
#           __add__(string, Order) <- not workable
#           __radd__(self, string)
print(new_order._cart)
print(order._cart)
order += "mango"
print(order._cart)