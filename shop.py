import json
import sys
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, opisanie, count = 100):
        self.name = name
        self.price = price
        self.opisanie = opisanie
        self.count = count

    @abstractmethod
    def get_discount(self) -> float: pass

    @abstractmethod  
    def get_info(self): pass

    def __str__(self) -> str:
        return f'{self.name} {self.count}'
    
    def to_dict(self):
        """Converts the Product object attributes to a dictionary."""
        return {
            "name": self.name,
            "price": self.price,
            "opisanie": self.opisanie,
            "count": self.count,
        }    

class Catalogue:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Adds a product to the catalogue."""
        self.products.append(product)

    def to_dict(self):
        """Converts the Catalogue object and its products to a dictionary."""
        return {"products": [product.to_dict() for product in self.products]}



class Vodka(Product):
    def __init__(self, name, price, opisanie, castle, count = 100):
        super().__init__(name, price, opisanie, count)
        self.castle = castle
        

    def get_discount(self): 
        return self.price - self.price / 100 * int(input("%"))

    def get_info(self):
        return self.opisanie

    def __str__(self) -> str:
        return f'{self.name} {self.count}'


class Laptop(Product):
    def __init__(self, name, price, opisanie, processor, count = 100):
        super().__init__(name, price, opisanie, count)
        self.processor = processor
        

    def get_discount(self): 
        return self.price - self.price / 100 * int(input("%"))

    def get_info(self):
        return self.opisanie

    def __str__(self) -> str:
        return f'{self.name} {self.count}'


class User():
    users = []
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.balance = 0
        self.cart: list[Product] = []
        self.role = ''
          

    def Change_password(self):
        inputPass = input("Введите пароль: ")
        if self.password != inputPass:
            self.password = inputPass
        else: print("Невозможно ввести идентичный пароль")

    def Buy(self, product):
        self.cart.append(product)
        if type(product) is Vodka:
            product.count -= 1
        if type(product) is Laptop:
            product.count -= 1
    
    @staticmethod
    def serialize(user):
        with open('users.json', 'r') as f: 
            User.users = json.load(f.read())
    

class Client(User):
    def __init__(self, login, password) -> None:
        super().__init__(login, password)


class Admin(User):
    def __init__(self, login, password) -> None:
        super().__init__(login, password) 

    def addProduct(self, product: Product):
        pass


    def deleteProduct(self, product: Product):
        pass

def serialize_catalogue_to_json(catalogue_file, catalogue):
    """Serializes the catalogue object and its products to a JSON file."""
    with open(catalogue_file, "w", encoding='utf-8') as f:
        json.dump(catalogue.to_dict(), f, indent=4)

catalogue = Catalogue()
CurrentUser: User = None

Op = User('Login', 'Password')
Exit = False
if __name__ == "__main__": 
    while not Exit:
        print(''' 
                ДОБРО ПОЖАЛОВАТЬ!!!
            ВЫБОР ДЕЙСТВИЯ:
            1 - АВТОРИЗОВАТЬСЯ
            2 - ЗАРЕЗЕРВИРОВАТЬСЯ
            3 - ВЫХОД!!!
        ''')
        Action = int(input("ВЫБОР: "))
        with open('users.json', 'r') as f: 
            try:
                User.users = json.load(f)
            except: pass
        match(Action):
            case 1:
                login = input("Login: ")
                password = input("Password: ")
                for i, user in enumerate(User.users):
                    if user['login'] == login and user['password'] == password:
                        CurrentUser = User(login, password)
                        print(f'ВЫ ВАШЛИ как {CurrentUser.login}!')
                    elif i==len(User.users) and CurrentUser == None: 
                        print('Ошибка авторизации')
                        break
                break
            case 2:
                print('Пж введите данные для регистрации аккаунта: ')
                Name = input('Имя пользователя: ')
                login = input("Login: ")
                password = input("Password: ")
                for user in User.users:
                    if user['login'] == login:
                        print('Такой пользователь уже есть иди отсюда((')
                        break
                    
                CurrentUser = User(login, password)

                with open('users.json', 'w') as f:
                    User.users.append({
                        "login": CurrentUser.login,
                        "password": CurrentUser.password
                    })
                    json.dump(User.users, f)
                print("Вы добавились как ",Name)
                break
            case 3:
                print('ДО СВИДАНИЯ!')
                sys.exit(0)
