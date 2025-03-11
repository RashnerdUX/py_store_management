import csv

class Item:
    discount = 0.8 #this is a class attribute
    all = [] #This contains all instances
    def __init__(self, name:str, price: float = 0.0, quantity: int = 0):
        assert price >= 0
        assert quantity >= 0

        self.name = name #These are instance attributes
        self.price = price
        self.quantity = quantity

        # Add to the all list
        Item.all.append(self)

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}

    @classmethod
    def save_to_csv(cls):
        with open("save_file.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
            print("About to save files")
            writer.writeheader()
            for item in cls.all:
                writer.writerow(item.to_dict())
            print("Files succesfully saved")

    @classmethod
    def load_from_csv(cls):
        with open("save_file.csv", "r") as file:
            reader = csv.DictReader(file)
            print("Loading files")
            items = list(reader)

        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )
        print("Files loaded successfully")

class Laptop(Item):
    all = []
    def __init__(self, processor: str, ram: int, storage: int, **kwargs):
        super().__init__(
            **kwargs
        )
        #Confirm data is clean
        assert ram >= 0
        assert storage >= 0

        #Assign them to their attributes
        self.processor = processor
        self.ram = ram
        self.storage = storage

        #Perform an action on it
        Laptop.all.append(self)

pc = Laptop(processor="Intel Core i5", ram=8, storage=500, name="Dell Latitude 5400", price=330, quantity=3)
print(Laptop.total_price(pc))
print(pc.total_price())
print(Laptop.all)
Item.load_from_csv()
print(Item.all)


