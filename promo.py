import random
from files_enum import *
import json

class Json:
    @staticmethod
    def read():
        with open(Files.promocobes, "r") as file:
            return json.load(file) 
    
    @staticmethod
    def write(data):
        with open(Files.promocobes, "w") as file:
            json.dump(data, file)
    

class Code_Manager():
    def __init__(self):
        self.promo_codes= []

    def generate_code(self):
        hangul = [chr(char_code) for char_code in range(44032, 55204)]
        promo_code = ''.join(random.choice(hangul) for _ in range(5))
        return promo_code
    

    def add_code(self):
        new_promo = self.generate_code()
        self.promo_codes.append(new_promo)
        print("Добавлен промокод: ", new_promo)
        

    # foreach(var c in "Tom")
    # {
    #     Console.WriteLine(c);
    # }
        
    # for (int i = 1; i < 4; i++)
    # {
    #     Console.WriteLine(i);
    # }

    def del_code(self):
        print('Список кодов:')
        for i, code in enumerate(self.promo_codes):
            print(f"{i+1} - {code}") 
        choice = int(input("Введите номер промокода:")) - 1
        try: 
            self.promo_codes.pop(choice)
            print("Удалено успешно")
        except:
            print("Неверный номер")


manager = Code_Manager()

print(manager.promo_codes)
manager.add_code()
print(manager.promo_codes)
manager.del_code()
print(manager.promo_codes)




