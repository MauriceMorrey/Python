class Product():
    def __init__(self, Price, Item_name, Weight, Brand, Status):
        self.price = Price
        self.name = Item_name
        self.weight = Weight
        self.brand = Brand
        self.status = Status
    def sell(self):
        self.status = "Sold"
        return self
    def add_tax(self):
        self.price = (0.09 * self.price) + self.price
        return self
    def Return(self):
        if (self.status == "Defective"):
            self.price = 0
        elif(self.status == "For Sale"):
            self.price = self.price
        elif(self.status == "Used"):
            self.price = self.price - (0.20 * self.price)
        return self
    def display_info(self):
        print "Price is: " + str(self.price) + " Dollars"
        print "Item name is: " + str(self.name)
        print "Weight is: " + str(self.weight)
        print "Brand is: " + str(self.brand)
        print "Brand is: " + self.status
        return self

product1 = Product(250, "football boots", "750 grams", "Nike Magista", "Defective")
product2 = Product(50, "chelsea jersey", "100 grams", "Adidas", "For sale")

product1.Return().display_info()
product2.sell().display_info()
