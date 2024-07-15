import random

start_money = random.randint(1, 999)
start_energy = random.randint(1, 50)

class Man:

    def __init__(self, name):
        self.name = name
        self.money = start_money
        self.energy = start_energy
        self.cat = None
        self.house = None

    def __str__(self):
        return f'Это {self.name}. У него есть {self.money} долларов. Уровень его энергии: {self.energy}.'

    def take_cat_home(self, cat):
        self.energy -= 10
        self.cat = cat
        self.cat.moving(house=home)
        self.house = home
        print(f'{self.name} забрал {self.cat.name} домой')

    def buy_food(self, house):
        self.house = house
        if self.money >= 50:
            self.house.food += 50
            self.money -= 50
            print(f'{self.name} купил кошачью еду.')
        else:
            print('Денег нет, но вы держитесь')
            self.work()

    def work(self):
        if day < 20:
            self.money += 50
            self.energy -= 30
            print(f'{self.name} сходил на работу.')
        else:
            self.money += 100
            self.energy -= 20
            print(f'{self.name} сходил на более оплачиваемую работу.')

    def clean(self, house):
        self.house = house
        if self.energy >= 20:
            self.house.cleanliness -= 40
            self.energy -= 10
            print(f'{self.name} убрался в доме.')
        else:
            print(f'{self.name} слишком устал.')
            self.rest()

    def rest(self):
        self.energy += 40
        print(f'{self.name} пошел отдыхать.')

    def walking(self, house):
        self.house = house
        self.energy += 20
        self.money -= 20
        print(f'{self.name} прогулялся')

    def act(self, house):
        self.house = house
        dice = random.randint(1,6)
        if self.house.food <= 20:
            self.buy_food(house=home)
        elif self.house.cleanliness >= 40:
            self.clean(house=home)
        elif dice == 1 or dice == 2:
            self.rest()
        elif dice == 3 or dice == 4:
            self.walking(house=home)
        else:
            self.work()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 10
        self.house = None
        self.angry = False

    def __str__(self):
        return f'Это {self.name}. Уровень его сытости: {self.fullness}.'

    def moving(self, house):
        self.house = house
        print(f'{self.name} забрали домой.')

    def eat(self, house):
        self.house = house
        if self.house.food >= 10:
            self.fullness += 20
            self.house.food -= 10
            print(f'{self.name} поел.')
        else:
            print(f'{self.name} голоден.')

    def sleep(self):
        self.fullness -= 10
        print(f'{self.name} хорошо выспался.')

    def vandalize(self, house):
        self.house = house
        self.fullness -= 10
        self.house.cleanliness += 20
        print(f'{self.name} подрал обои.')

    def play(self, house):
        self.house = house
        dice = random.randint(1,6)
        if self.fullness <= 0 or self.house.cleanliness >= 200:
            print(f'{self.name} убежал.')
            self.angry = True
            return
        elif self.fullness <= 20:
            self.eat(house=home)
        elif dice == 1 or dice == 2 or dice == 3:
            self.sleep()
        else:
            self.vandalize(house=home)


class House:

    def __init__(self):
        self.food = 0
        self.cleanliness = 0

    def __str__(self):
        return f'Еды в кошачьей миске: {self.food}. Степень грязи в доме: {self.cleanliness}.'


inho = Man(name='Иннокентий')
kittens = [
        Cat(name='Суни'),
        Cat(name='Дуни'),
        Cat(name='Дори')
]

home = House()
for kitten in kittens:
    kitten.moving(house=home)

for day in range(1,366):
    print('========== День {} =========='.format(day))
    inho.act(house=home)
    for kitten in kittens:
        kitten.play(house=home)
    if kitten.angry == True:
        print('Конец игры')
        break
    print('-----------------------------')
    print(inho)
    print(home)
    for kitten in kittens:
        print(kitten)

if kitten.angry == False:
    print('Вы пережили год!')