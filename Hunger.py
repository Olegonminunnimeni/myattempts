import time
import asyncio
import os
import random
'''
async def tick():
    while True:
        await asyncio.sleep(1)  # Задержка на 1 секунду
        print("Tick")

async def main():
    asyncio.create_task(tick())  # Запуск задачи tick в фоновом режиме
    while True:
        await asyncio.sleep(2.5)  # Задержка на 0.5 секунды
        print("tock")

asyncio.run(main())
'''
'''
class MyClass:
    def __init__(self):
        self.__value = None
 
    @property
    def value(self):
        """This is 'value' property."""
        return self.__value
 
    @value.setter
    def value(self, value):
        if value > 2:
            self.__value = value
 
    
d = MyClass()
d.value = 10
print(d.value)
'''

class Doge:
    def __init__(self, health=100, attack=100, hunger=100, mind=100):
        self.health = health
        self.attack = attack
        self.__hunger = hunger
        self.mind = mind
        self.inventory = []

    @property
    def hunger(self): 
        return self.__hunger
    
    @hunger.setter
    def hunger(self, value):
        if self.hunger >= 100:
            self.hunger = 100
        else: 
            self.__hunger+=value

    async def golodanie(self):
        while True:
            await asyncio.sleep(3)  # Sleep for 5 seconds
            self.hunger -= 1
            # You can add logic here to check if hunger reaches 0 and take actions

    async def hunting(self):
        if True in self.inventory:
            Nomer = random.randint(1, 5)
            if True:
                self.hunger += 200
                await asyncio.sleep(4)
        else: return


    def Stats(self):
        print("Ваш голод:", self.hunger)
        print("Ваша ГОЛОВА:", self.mind)
        print("Ваш атак:", self.attack)
        print("Ваше життя:", self.health)


async def main():
    KOT = Doge()
    asyncio.create_task(KOT.golodanie())  # Start golodanie in the background
    asyncio.create_task(KOT.hunting())  # Start golodanie in the background

    while True:
        KOT.Stats()
        await asyncio.sleep(3)
        os.system('cls')  # Print stats every 5 seconds
        

if __name__ == "__main__":
    asyncio.run(main())
