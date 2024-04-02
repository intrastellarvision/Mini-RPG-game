import time
import random

class Hero():
    def __init__(self, lifes, intellect, strong, lovkost, name):
        self.lifes = lifes
        self.intellect = intellect
        self.strong = strong
        self.lovkost = lovkost
        self.name = name

    def weapon(self):
        if self.strong > self.intellect and self.strong > self.lovkost:
            weapon = "magicball"
        elif self.intellect > self.strong and self.intellect > self.lovkost:
            weapon = "magic"
        else:
            weapon = "MagicBall"
        return weapon

        def weapon(self):
            if self.strong > self.intellect and self.strong > self.lovkost:
                weapon = "epicbow"
            elif self.intellect > self.strong and self.intellect > self.lovkost:
                weapon = "magic"
            else:
                weapon = "EpicBow"
            return weapon

        def weapon(self):
            if self.strong > self.intellect and self.strong > self.lovkost:
                weapon = "sword"
            elif self.intellect > self.strong and self.intellect > self.lovkost:
                weapon = "magic"
            else:
                weapon = "MagicBall"
            return weapon
    
    def role(self):
        if self.strong > self.intellect and self.strong > self.lovkost:
            role = "swordmen"
        elif self.intellect > self.strong and self.intellect > self.lovkost:
            role = "mag"
        else:
            role = "bowler"
        return role

    def armor(weapon):
        if weapon == "sword":
            armor = 10
        elif weapon == "magic band":
            armor = 5
        else:
            armor = 4
        return armor

    def damage(self, weapon):
        if weapon == "sword":
            damage = random.randint(1,5)*self.strong
        elif weapon == "magic band":
            damage = random.randint(3,5)*self.intellect
        else:
            damage = random.randint(1,8)*self.lovkost
        return damage

        def damage(self, weapon):
            if weapon == "bow":
                damage = random.randint(1,5)*self.strong
            elif weapon == "magic":
                damage = random.randint(5,5)*self.intellect
            else:
                damage = random.randint(3,8)*self.lovkost
        return damage
    
        def damage(self, weapon):
            if weapon == "magicball":
                damage = random.randint(6,5)*self.strong
            elif weapon == "magic":
                damage = random.randint(3,5)*self.intellect
            else:
                damage = random.randint(9,8)*self.lovkost
        return damage


MyHero = Hero(300, 10, 5, 6, "Barista")
Enemy = Hero(200, random.randint(1,5), random.randint(1,6), random.randint(1,5), "Venom")
print("Приветствую в сражении героев")
while MyHero.lifes >= 0:
    print("Ваше имя", MyHero.name, "Ваше спецификация", MyHero.role(),"Жизни", MyHero.lifes)
    print("Броня", MyHero.armor(), "Оружие", MyHero.weapon(), "Урон", MyHero.damage(MyHero))
    print("/nИмя врага", Enemy.name, "Ваше спецификация", Enemy.role(),"Жизни", Enemy.lifes)
    print("Броня", Enemy.armor(), "Оружие", Enemy.weapon(), "Урон", Enemy.damage(Enemy))
    MyHero.lifes -= Enemy.damage(Enemy)
    Enemy.lifes -= MyHero.damage(MyHero)
    time.sleep(2)
