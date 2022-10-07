class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(f'welcome to {self.restaurant_name}')
        print(f"At {self.restaurant_name} we server only {self.cusine_type} dishes")
    def open_restaurant(self):
        print(f'we are open for business')
    def customers_served(self):
        print(f'we have served {self.number_served} customers so far')
restaurant = Restaurant('vikels', 'continetal')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.customers_served()

class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cusine_type):
        super().__init__(restaurant_name, cusine_type)
        self.flavors = ['vanilla','strawbery','lollies']
    #method to display flavours
    def show_flav(self):
        print(f'these are the list of icecream flavours we server: {self.flavors}')
#create an instance or object
juiccey = IcecreamStand('vikels', 'icecream')
juiccey.show_flav()
        