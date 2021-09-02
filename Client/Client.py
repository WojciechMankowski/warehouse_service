from collections import Counter
from dataclasses import dataclass
from uuid import uuid4
@dataclass
class NewClient:
    id: str

class Client:

    def __init__(self):
        self.order = Counter()
        self.price = Counter()
        self.orderSum = []
        id = str(uuid4())
        self.new_client = NewClient(id)

    def SaveInDict(self, name: str, weight: float) -> None:
        order = {f'{name}': weight}
        self.order.update(order)
        print(self.order)

    def OrderSummary(self, unit: dict[str, str], price: dict[str, float]):
        listaSummary = []
        for key, item in self.order.items():
            self._CountingThePrice(key, price[key], item)
            listaSummary.append(f"{key}: {item} {unit[key]} -> {self.price[key]}")
        listaSummary.append(f"Całkowita suma zamówienia: {sum(self.orderSum)}")
        return listaSummary

    def _CountingThePrice(self, name, price, scales):
        Price = round(price * scales, 2)
        self.price.update({f"{name}": Price})
        self.orderSum.append(Price)

    def SubmitAnOrder(self):
        order_submit = {f"{self.new_client.id}": self.order}
        return order_submit

    def BoolenWeight(self, name, weight, dictionary_with_weight):
        how = dictionary_with_weight[name]
        print(how > weight)
        if how > weight:
            return True
        return False




