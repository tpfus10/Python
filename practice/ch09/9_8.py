class Privileges:
    def __init__(self):
        self.privileges = ['can delete', 'can add post', 'can ban user']
    
    def show_privileges(self):
        for previlege in self.privileges:
            print(previlege)

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

class Admin(User):
    def __init__(self, fname, lname, agee, resedence):
        super().__init__(fname, lname, agee, resedence)
        self.privileges = Privileges()

new_admin = Admin('Amy', 'Olive', 22, 'cali')
print(new_admin.describe_user())
print(new_admin.privileges.show_privileges()) 
#클래스1의 인스턴스를 클래스2의 속성으로 만들면 
#'클래스2의 인스턴스.클래스1의 변수명.클래스1의 함수명' 형식으로 호출해야 함
