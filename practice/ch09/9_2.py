class Restaurant:
    def __init__(self, rname, ctype): 
        self.restaurant_name = rname
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"{self.cuisine_type} restaurant's name is {self.restaurant_name}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant1 = Restaurant('Fallet', 'Italian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2 = Restaurant('Umaido', 'Japanese')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant2 = Restaurant('한 그릇', 'Korean')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

