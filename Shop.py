from Functions import *
from Gacha import gachaMenu


#wait a sec this class is useless isn't it
class purchasable():
    def __init__(self, name, price):
        self.name = name
        self.price = price

class equipable(purchasable):
    def __init__(self, name, price, isBought):
        super(equipable, self).__init__(name, price)
        self.isBought = isBought

class weaponn(equipable):
    def __init__(self, name, price, isBought, minAttack, maxAttack):
        super(weaponn, self).__init__(name, price, isBought)
        self.minAttack = minAttack
        self.maxAttack = maxAttack

class armour(equipable):
    def __init__(self, name, price, isBought, healthIncrease):
        super(armour, self).__init__(name, price, isBought)
        self.healthIncrease = healthIncrease

class accessory(equipable):
    def __init__(self, name, price, isBought, regen):
        super(accessory, self).__init__(name, price, isBought)
        self.regen = regen

# the isBought variable is unused because I wrote it then realised I don't know how to use it


def buy(player, item, type):
    print("Gold: {}".format(player.gold))
    print("(1) Buy {} ({}g)".format(item.name, item.price))
    print("(2) Quit")
    buyInput = integer_input(2)
    if buyInput == 1:
        if player.gold >= item.price:
            player.gold -= item.price
            if type == "weapon":
                player.weaponTier += 1
            elif type == "hat":
                player.hatTier += 1
            elif type == "armour":
                player.armourTier += 1
            elif type == "accessory":
                player.accessoryTier += 1
            input("You have bought {}".format(item.name))
        else:
            input("You do not have enough money")


def shop(player):
    shopRun = True
    shopMenu = ["Gear", "Potions", "Gacha", "Main Menu"]
    equipsMenu = ["Weapon", "Helmet", "Armour", "Accessory", "Back"]
    consumablesMenu = ["Health Potion (10g)", "Max Health Potion (100g)", "Back"]
    HEALTHPOTIONCOST = 10
    MAXHEALTHPOTIONCOST = 100


    # weapons
    # this doesn't work when weapon has 1 n and idk why
    woodSword = weaponn("Wood Sword", 75, False, 3, 6)
    ironSword = weaponn("Iron Sword", 500, False, 8, 10)
    platSword = weaponn("Platinum Sword", 1500, False, 30, 40)

    # hats
    woodHelmet = armour("Wood Helmet", 50, False, 8)
    ironHelmet = armour("Iron Helmet", 400, False, 18)
    platHelmet = armour("Platinum Helmet", 1000, False, 30)

    # armours
    woodArmour = armour("Wood Armour", 100, False, 10)
    ironArmour = armour("Iron Armour", 1000, False, 22)
    platArmour = armour("Platinum Armour", 2000, False, 50)

    # accessories (maybe add an armour as the last one here)
    regenBand = accessory("Regen Band", 1000, False, 5)
    superRegenBand = accessory("Super Regen Band", 2000, False, 10)


    hatList = [woodHelmet, ironHelmet, platHelmet]
    armourList = [woodArmour, ironArmour, platArmour]
    weaponList = [woodSword, ironSword, platSword]
    accessoryList = [regenBand, superRegenBand]

    #buy potions
    def buy_potions(potionCost, potionName):
        print("Select amount to buy")
        buyQuantity = integer_input(100)
        if player.gold >= potionCost * buyQuantity:
            player.gold -= potionCost * buyQuantity
            player.healthPotion += buyQuantity
            input("Bought {} {}s" .format(buyQuantity, potionName))
        else:
            input("You do not have enough money")


    # loop for shop
    while shopRun == True:
        print("Shop Menu")
        print("Gold: {}".format(player.gold))
        print_list(shopMenu)
        shopInput = integer_input(len(shopMenu))
        #this is the gear button
        if shopInput == 1:
            gearRun = True
            while gearRun == True:
                print_list(equipsMenu)
                secondInput = integer_input(len(equipsMenu))
                if secondInput == 1:
                    if player.weaponTier == 0:
                        buy(player, woodSword, "weapon")
                    elif player.weaponTier == 1:
                        buy(player, ironSword, "weapon")
                    elif player.weaponTier == 2:
                        buy(player, platSword, "weapon")
                elif secondInput == 2:
                    if player.hatTier == 0:
                        buy(player, woodHelmet, "hat")
                    elif player.hatTier == 1:
                        buy(player, ironHelmet, "hat")
                    elif player.hatTier == 2:
                        buy(player, platHelmet, "hat")
                elif secondInput == 3:
                    if player.armourTier == 0:
                        buy(player, woodArmour, "armour")
                    elif player.armourTier == 1:
                        buy(player, ironArmour, "armour")
                    elif player.armourTier == 2:
                        buy(player, platArmour, "armour")
                elif secondInput == 4:
                    if player.accessoryTier == 0:
                        buy(player, regenBand, "accessory")
                    elif player.accessoryTier == 1:
                        buy(player, superRegenBand, "accessory")
                elif secondInput == 5:
                    gearRun = False
        #this is the potion button
        if shopInput == 2:
            potionRun = True
            while potionRun == True:
                print("Potions: You can bring up to five of each type to your adventure")
                print("Gold: {}".format(player.gold))
                print("Owned: {} Health Potion\t{} Max Health Potion" .format(player.healthPotion, player.maxHealthPotion))
                print_list(consumablesMenu)
                secondInput = integer_input(len(consumablesMenu))
                if secondInput == 1:
                    buy_potions(HEALTHPOTIONCOST, "health potion")
                if secondInput == 2:
                    buy_potions(MAXHEALTHPOTIONCOST, "max health potion")
                if secondInput == 3:
                    potionRun = False
        #this is the gacha button
        if shopInput == 3:
            if player.forestFirstClear == False:
                gachaMenu(player)
            else:
                input("You haven't unlocked this feature yet")
        if shopInput == 4:
            shopRun = False

    # calculates player stats
    # health
    player.maxHealth = 20
    if player.hatTier == 1:
        player.maxHealth += woodHelmet.healthIncrease
    elif player.hatTier == 2:
        player.maxHealth += ironHelmet.healthIncrease
    elif player.hatTier == 3:
        player.maxHealth += platHelmet.healthIncrease
    if player.armourTier == 1:
        player.maxHealth += woodArmour.healthIncrease
    elif player.armourTier == 2:
        player.maxHealth += ironArmour.healthIncrease
    elif player.armourTier == 3:
        player.maxHealth += platHelmet.healthIncrease

    # attack
    if player.weaponTier == 0:
        player.minAttack = 2
        player.maxAttack = 4
    elif player.weaponTier == 1:
        player.minAttack = woodSword.minAttack
        player.maxAttack = woodSword.maxAttack
    elif player.weaponTier == 2:
        player.minAttack = ironSword.minAttack
        player.maxAttack = ironSword.maxAttack
    elif player.weaponTier == 3:
        player.minAttack = platSword.minAttack
        player.maxAttack = platSword.maxAttack

    # regen
    if player.accessoryTier == 0:
        player.regen = 1
    if player.accessoryTier == 1:
        player.regen = regenBand.regen
    if player.accessoryTier == 2:
        player.regen = superRegenBand.regen
