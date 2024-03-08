class Restaurant:
    def __init__(self, rname, ctype): 
        self.restaurant_name = rname
        self.cuisine_type = ctype

    def describe_restaurant(self):
        print(f"{self.cuisine_type} restaurant's name is {self.restaurant_name}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

#클래스 상속
class IceCreamStand (Restaurant):
    def __init__(self, rname, ctype, flavors):
        super().__init__(rname, ctype)
        self.flavors = flavors

    def show_flavors(self):
        print("The flavor is {}".format(self.flavors))
        print(f"The flavor is {self.flavors}")

#인스턴스 생성
ice_cream = IceCreamStand('yummy', 'icecream', 'vanila')

#메서드 호출
ice_cream.show_flavors()