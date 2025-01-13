from dataclasses import dataclass


@dataclass()
class Product:
    id: str
    name: str
    price: float


    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}