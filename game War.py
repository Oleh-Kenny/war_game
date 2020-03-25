from random import randint
import random

class Unit:
    def __init__(self, name, hp, damag, dodge):
        self.__name = name
        self.__hp = hp
        self.__damag = damag
        self.__dodge = dodge


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp
        return self.__hp

    @property
    def damag(self):
        return self.__damag

    @damag.setter
    def damag(self, damag):
        self.__damag = damag
        return self.__damag

    @property
    def dodge(self):
        return self.__dodge

    @dodge.setter
    def dodge(self, dodge):
        self.__dodge = dodge
        return self.__dodge

class Swordsman(Unit):
    def __init__(self, name = "Swordsman", hp = 20, damag = 7, dodge = 60):
        self.name = str(name)
        self.hp = int(hp)
        self.damag = int(damag)
        self.dodge = int(dodge)

class Archer(Unit):
    def __init__(self, name = "Archer", hp = 15, damag = 5, dodge = 50):
        self.name = str(name)
        self.hp = int(hp)
        self.damag = int(damag)
        self.dodge = int(dodge)

class Mage(Unit):
    def __init__(self, name = "Mage", hp = 10, damag = 8, dodge = 70):
        self.name = str(name)
        self.hp = int(hp)
        self.damag = int(damag)
        self.dodge = int(dodge)

def main():
    player = []
    computer = []

    for i in range(3):
        x = random.randint(0, 2)
        if x == 0:
            player.append(Swordsman())
        elif x == 1:
            player.append(Archer())
        elif x == 2:
            player.append(Mage())

    for j in range(3):
        x = random.randint(0, 2)
        if x == 0:
            computer.append(Swordsman())
        elif x == 1:
            computer.append(Archer())
        elif x == 2:
            computer.append(Mage())

    return player, computer


def start():
    opponents = main()
    player = opponents[0]
    computer = opponents[1]
    hp_player = player[0].hp + player[1].hp + player[2].hp
    hp_computer = computer[0].hp + computer[1].hp + computer[2].hp
    print("Початок Війни")
    print("Команда Гравця: ", hp_player, "\nКоманда Компютера: ", hp_computer)


    while hp_player > 0 and hp_computer > 0:
        choice_first = random.randint(0, 1)
        choice_warriors_attack = random.randint(0, 2)
        choice_warrior_protection = random.randint(0, 2)
        if choice_first == 0:
            print("Атакує Гравець")
            input("\nНатисніть Enter для продовження")
            if choice_warriors_attack == 0:
                attacks = player[0]
            elif choice_warriors_attack == 1:
                attacks = player[1]
            elif choice_warriors_attack == 2:
                attacks = player[2]

            if choice_warrior_protection == 0:
                protected = computer[0]
            elif choice_warrior_protection == 1:
                protected = computer[1]
            elif choice_warrior_protection == 2:
                protected = computer[2]

            print(attacks.name, "Команда Гравця атакує", protected.name , "Компютера")
            fortuna = randint(1, 100)
            if fortuna > protected.dodge:
                print("Атака вдалася")
                print(protected.name, "втрачає" , attacks.damag, "життів")
                hp_computer = hp_computer - attacks.damag
                print("Команда гравця: ", hp_player, "\nКоманда Компютера: ", hp_computer)
                print("--------------------------------------")

            else:
                print("Атака невдалася. Захист спрацював")
                print("--------------------------------------")

        else:
            print("\nАтака Компютера")
            input("\nНажміть Enter для продовження")
            if choice_warriors_attack == 0:
                attacks = computer[0]
            elif choice_warriors_attack == 1:
                attacks = computer[1]
            elif choice_warriors_attack == 2:
                attacks = computer[2]

            if choice_warrior_protection == 0:
                protected = player[0]
            elif choice_warrior_protection == 1:
                protected = player[1]
            elif choice_warrior_protection == 2:
                protected = player[2] 
        
            print(attacks.name, "Команда Компютера атакує", protected.name , "Гравця")
            fortuna = randint(1, 100)
            if fortuna > protected.dodge:
                print("Атака вдалася")
                print(protected.name, "втрачає" , attacks.damag, "життів")
                hp_player = hp_player - attacks.damag
                print("Команда гравця: ", hp_player, "\nКоманда Компютера: ", hp_computer)
                print("--------------------------------------")

            else:
                print("Атака невдалася. Захист спрацював")
                print("--------------------------------------")

            
    if hp_player == 0:
        print("------ Кінець Гри -------")
        print("------ Виграє Команда Компютера ------")
    else:
        print("------ Кінець Гри -------")
        print("------ Виграє Команда Гравця ------")

exit = False
while not exit:
    print("---------- Гравець проти Компютера ----------")
    try:
        choise = int(input("1. Старт Гри\n0. Вихід\n"))
        if choise == 1:
            main()
            start()

        elif choise == 0:
            exit = True
        else:
            print("Читайте Умову")
    except Exception as error:
        print("Помилка --> ", error)
