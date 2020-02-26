import random

weapons_list = ['sword','dagger', 'crossbow']
lst = ['hammer', 'bow', 'gun', 'whip', 'staff', 'brass knuckles']
selected_weapon = random.choice(weapons_list)

class Weapon():
    def __init__(self):
        print('A weapon has been forged!')
        print(f'The forged weapon is {selected_weapon}')

my_weapon = Weapon()

class Dagger(Weapon):

    def __init__(self, speed, damage, type):
        pass

    def stats(self, speed=8, damage=4, weap_type='Melee'):
        self.speed = speed
        self.damage = damage
        self.weap_type = weap_type

a_dagger = Dagger()

class Sword(Weapon):

    def __init__(self, speed, damage, type):
        pass

    def stats(self, speed=5, damage=6, weap_type='Melee'):
        self.speed = speed
        self.damage = damage
        self.weap_type = weap_type

a_sword = Sword()


class Crossbow(Weapon):

    def __init__(self, speed, damage, type):
        pass

    def stats(self, speed=6, damage=4, weap_type='Range'):
        self.speed = speed
        self.damage = damage
        self.weap_type = weap_type

a_crossbow = Crossbow()
