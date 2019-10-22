from Functions import *
from Game import game
from Shop import shop
from Equip import equip


class player:
    def __init__(self):
        self.maxHealth = 20
        self.health = self.maxHealth
        self.regen = 1
        self.minAttack = 2
        self.maxAttack = 4
        self.gold = 0
        self.gachaToken = 0
        self.name = ""

        #teleporting
        self.teleporter = 0
        self.forestFirstClear = True
        self.caveFirstClear = True
        self.swampFirstClear = True

        #don't need to load these
        self.hawkGatlingCharge = [0, 0] # [charge, minDamage, maxDamage]
        self.skipStage = False

        # store
        self.weaponTier = 0
        self.hatTier = 0
        self.armourTier = 0
        self.accessoryTier = 0
        self.healthPotion = 0
        self.maxHealthPotion = 0
        self.carryHealthPotion = 0
        self.carryMaxHealthPotion = 0

        # gems (numbers should be 0 unless if testing)
        self.rabbit = 0
        self.tank = 0
        self.gorilla = 0
        self.diamond = 0
        self.hawk = 0
        self.gatling = 0
        self.ninja = 0
        self.comic = 0
        self.dragon = 0
        self.lock = 0

        # gem equip, based on level (numbers should be 0 unless if testing)
        self.rabbitEquip = 0
        self.tankEquip = 0
        self.gorillaEquip = 0
        self.diamondEquip = 0
        self.hawkEquip = 0
        self.gatlingEquip = 0
        self.ninjaEquip = 0
        self.comicEquip = 0
        self.dragonEquip = 0
        self.lockEquip = 0

player = player()
gameRun = True

while gameRun == True:
    print("WELCOME TO GAME")
    name = input("Enter Name: ")
    player.name = name

    while gameRun == True:
        # MAIN MENU
        print("Main Menu")
        print("(1) Start Adventure")
        print("(2) Shop")
        print("(3) Equip")
        print("(4) Exit Game")
        menuInput = integer_input(4)
        if menuInput == (1):
            game(player)
        elif menuInput == (2):
            shop(player)
        elif menuInput == (3):
            equip(player)
        elif menuInput == (4):
            print("Bye")
            gameRun = False
