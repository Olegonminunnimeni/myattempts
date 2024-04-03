import hashlib
from crypto.cipher import AES
from crypto.Util.Padding import pad, unpad

class User():
    def __init__(self, login, password):
        self.login = login
        self.password = password
Chicha = User("lgn", "passwrd")


class Dementia():
    def __init__(self, key, algorythm="AES"):
        self.key = key
        self.algorythm = algorythm

    
    def encrypt(self, password):
        cipher = AES.new(self.key, AES.MODE_ECB)
        padded_password = pad(password.encode(), AES.block_size)
        encrypted_password = cipher.encrypt(padded_password)
        return encrypted_password
    
    def decrypt(self, password):
        pass
                

Oldman = Dementia()
Censoredpass = Oldman.encrypt(Chicha.password)
print(Censoredpass)
    