class ShoppingCart:
    def __init__(self):
        self.items={}
        self.total=0

    def add_item(self,item_name,quantity,price):
        cost= quantity*price
        self.total+=cost
        self.items[item_name]=quantity


    def remove_item(self, item_name, quantity, price):
        quantity_in_cart= self.items[item_name]
        if quantity>=quantity_in_cart:
            del self.items[item_name]
            self.total=quantity_in_cart*price
        else:
            self.items[item_name] = quantity_in_cart-quantity
            self.total = quantity * price

    def checkout(self,cash_paid):
        if self.total>cash_paid:
            return cash_paid
        elif cash_paid==self.total:
            return  0
        else:
            return  cash_paid-self.total

class Shop(ShoppingCart):
    def __init__(self):
        self.quantity=100

    def remove_item(self):
        self.quantity-=1






