import hashlib


class User():
    def __init__(self, login, password):
        self.login = login
        self.password = password
Anon = User("Anon228", "Anontop")

class Hash():
    def __init__(self, algorithm = 'sha-256'):
        self.algorithm = algorithm
    def Hashi(self, example):
        hasher = hashlib.new(self.algorithm)
        hasher.update(example.encode('utf-8'))
        hasher_example = hasher.hexdigest()
        return hasher_example
    
example = "Koko Jambo"
Hastler = Hash()
hasher_example = Hastler.Hashi(example)
print(hasher_example)
Example2 = Anon.password
hasher_example2 = Hastler.Hashi(Example2)
print(hasher_example2)