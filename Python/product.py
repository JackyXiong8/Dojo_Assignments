

class product:
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        print (self.price, self.item_name, self.weight, self.brand, self.status)
        return self
    def addTax(self, tax):
        self.price = (self.price,tax)
        return self
    def Return(self, reason):
        if reason == "defective":
            self.price = 0
            self.status = "defective"
        if reason == "box":
            self.status = "for sale"
        if reason == "opened":
            self.status = "used"
            self.price = self.price * 0.8
        return self
    def display_info(self):
        print (self.price, self.item_name, self.weight, self.brand, self.status)
        return self
    
product1 = product(10, "Cabbage", "1lb", "walmart")

product1.addTax(.8).display_info()

