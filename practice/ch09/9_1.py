class Restaurant:
    def __init__(self, rname, ctype): 
        self.restaurant_name = rname
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"{self.cuisine_type} restaurant's name is {self.restaurant_name}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant = Restaurant('Fallet', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()