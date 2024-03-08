class User:
    def __init__(self, fname, lname, agee, residencee):
        self.first_name = fname
        self.last_name = lname
        self.age = agee
        self.residence = residencee

    def describe_user(self):
        print(f"{self.first_name}{self.last_name} is {self.age} and live in {self.residence}.")

    def greet_user(self):
        print(f"Wellcome to our school, {self.first_name} {self.last_name}!")

freshman = User('James', 'cameron', 20, 'NewYork')
freshman.describe_user()
freshman.greet_user() 