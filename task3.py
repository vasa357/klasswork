class Order():
    def __init__(self, date, number):
        self.date = date
        self.number =number 
    
    def __str__(self):
        return f"Order {self.date} | {self.number}"
    
    def confirm(self):
        print(f"Order {self.number} comfirmed")
    
    def close(self):
        print(f"Order {self.number} closed")

class SpecialOrder(Order):
    def __init__(self, date, number, private_client):
        super().__init__(date, number)
        self.private_client = private_client
    
    def dispatch(self):
        print(f"SpecialOrder: {self.number} dispatched")
        

class NormalOrder(Order):
    def dispatch(self):
        print(f"NormalOrder: {self.number} dispatched")
    
    def recive(self):
        print(f"NormalOrder: {self.number} recived")
    

class Customer():
    def send_order(self, order):
        print(f"Customer {self.name} sends order {order}")
    
    def __str__(self):
        return f"Customer {self.date} | {self.number}"
    
    def receive_order(self, order):
        print(f"Customer {self.name} receives order {order}")
        
customer = Customer("Peter Parker", '123 main street')
order = NormalOrder('08.03.2024', 12345)
customer.send_order(order)