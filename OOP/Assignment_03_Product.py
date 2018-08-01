class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self, tax):
        sales_tax = self.price * tax
        self.price += sales_tax
        return self
    def returnItem(self, reason):
        if reason == "defective":
            self.status = reason
            self.price = 0
            return self
        elif reason == "like new":
            self.status = "for sale"
            return self
        elif reason == "opened":
            self.status = "used"
            self.price *= 0.8
            return self
    def dispaly_info(self):
        print "Price: {}".format(self.price)
        print "Item Name: {}".format(self.item_name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Status: {}".format(self.status)
        return "***********************"

product1 = Product(100, "1 TB Flash Drive", "0.2 lbs", "SanDisk")
print product1.dispaly_info()
print product1.addTax(0.06).sell().dispaly_info()
print product1.returnItem("opened").dispaly_info()