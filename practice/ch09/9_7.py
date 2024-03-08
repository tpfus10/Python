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

class Privileges:
    def __init__(self):
        #문자열로 이루어진 리스트 속성 privileges를 추가
        self.privileges = ['can delete', 'can add post', 'can ban user']
    
    def show_privileges(self):
        for previlege in self.privileges:
            print(previlege)

class Admin(User):
    def __init__(self, fname, lname, agee, resedence):
        super().__init__(fname, lname, agee, resedence)
        self.privileges = Privileges()


admin = Admin('jason', 'bond', 30, 'LA')
admin.privileges.show_privileges()