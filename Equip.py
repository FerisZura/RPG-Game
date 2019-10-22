from Functions import *


# prints a gem if it is owned. prints (E) after if it is equipped
def print_gem(gemCount, equipped, string):
    if equipped == 0:
        if gemCount > 0 and gemCount < 3:
            print(string)
        elif gemCount >= 3 and gemCount < 6:
            print(string + " LV2")
        elif gemCount >= 6:
            print(string + " LV3")
    if equipped > 0:
        if gemCount > 0 and gemCount < 3:
            print(string + " (E)")
        elif gemCount >= 3 and gemCount < 6:
            print(string + " LV2 (E)")
        elif gemCount >= 6:
            print(string + " LV3 (E)")


# flips a gem between equipped and non equipped. Only when the number of gems equipped is 6 or less
def select_gem(gemCount, equipped, gemName, numberEquipped):
    if equipped == 0:
        if numberEquipped >= 6:
            input("You have the max number of gems equipped!")
            return equipped, numberEquipped
        else:
            if gemCount > 0 and gemCount < 3:
                input("You have equipped the {} gem".format(gemName))
                return 1, numberEquipped + 1
            elif gemCount >= 3 and gemCount < 6:
                input("You have equipped the {} gem (LV2)".format(gemName))
                return 2, numberEquipped + 1
            elif gemCount >= 6:
                input("You have equipped the {} gem (LV3)".format(gemName))
                return 3, numberEquipped + 1
    elif equipped > 0:
        input("You have unequipped the {} gem".format(gemName))
        return 0, numberEquipped - 1


def equip(player):
    equipRun = True
    equipMenu = ["View stats", "Equip gems", "About gems", "Main Menu"]
    numberEquipped = 0
    # ^^pay attention to this pls
    ################################################################################
    # make initialize function where it runs through all gems and sees if equipped  #
    ################################################################################

    while equipRun == True:
        print("Equip Menu")
        print_list(equipMenu)
        menuInput = integer_input(len(equipMenu))
        if menuInput == 1:
            print("{}'s Stats".format(player.name))
            print("Weapon level: {}".format(player.weaponTier))
            print("Helmet level: {}".format(player.hatTier))
            print("Armour level: {}".format(player.armourTier))
            print("Max health: {}".format(player.maxHealth))
            print("Min attack: {}".format(player.minAttack))
            print("Max attack: {}".format(player.maxAttack))
            print("Health potions: {}" .format(player.healthPotion))
            print("Super health potions: {}" .format(player.maxHealthPotion))
            input("Equipped Gems: Can be viewed from [Equip gems]")
            print()
        elif menuInput == 2:
            gemLoop = True
            print("Type input to equip/unequip gem. Can equip up to six")
            while gemLoop == True:
                # display owned and unequipped gems hmm spaghetti
                print_gem(player.rabbit, player.rabbitEquip, "(r) Rabbit Gem")
                print_gem(player.tank, player.tankEquip, "(t) Tank Gem")
                print_gem(player.gorilla, player.gorillaEquip, "(go) Gorilla Gem")
                print_gem(player.diamond, player.diamondEquip, "(di) Diamond Gem")
                print_gem(player.hawk, player.hawkEquip, "(h) Hawk Gem")
                print_gem(player.gatling, player.gatlingEquip, "(ga) Gatling Gem")
                print_gem(player.ninja, player.ninjaEquip, "(n) Ninja Gem")
                print_gem(player.comic, player.comicEquip, "(c) Comic Gem")
                print_gem(player.dragon, player.dragonEquip, "(dr) Dragon Gem")
                print_gem(player.lock, player.lockEquip, "(l) Lock Gem")
                print("(q)(4) Quit")
                gemInput = input()
                gemInput = gemInput.lower()

                # equip/unequips gem
                if gemInput == "r":
                    player.rabbitEquip, numberEquipped = select_gem(player.rabbit, player.rabbitEquip, "rabbit",
                                                                    numberEquipped)
                elif gemInput == "t":
                    player.tankEquip, numberEquipped = select_gem(player.tank, player.tankEquip, "tank", numberEquipped)
                elif gemInput == "go":
                    player.gorillaEquip, numberEquipped = select_gem(player.gorilla, player.gorillaEquip, "gorilla",
                                                                     numberEquipped)
                elif gemInput == "di":
                    player.diamondEquip, numberEquipped = select_gem(player.diamond, player.diamondEquip, "diamond",
                                                                     numberEquipped)
                elif gemInput == "h":
                    player.hawkEquip, numberEquipped = select_gem(player.hawk, player.hawkEquip, "hawk", numberEquipped)
                elif gemInput == "ga":
                    player.gatlingEquip, numberEquipped = select_gem(player.gatling, player.gatlingEquip, "gatling",
                                                                     numberEquipped)
                elif gemInput == "n":
                    player.ninjaEquip, numberEquipped = select_gem(player.ninja, player.ninjaEquip, "ninja",
                                                                   numberEquipped)
                elif gemInput == "c":
                    player.comicEquip, numberEquipped = select_gem(player.comic, player.comicEquip, "comic",
                                                                   numberEquipped)
                elif gemInput == "dr":
                    player.dragonEquip, numberEquipped = select_gem(player.dragon, player.dragonEquip, "dragon",
                                                                    numberEquipped)
                elif gemInput == "l":
                    player.lockEquip, numberEquipped = select_gem(player.lock, player.lockEquip, "lock", numberEquipped)
                elif gemInput == "q" or gemInput == "4":
                    gemLoop = False
                else:
                    input("Invalid input")

        elif menuInput == 3:
            gemDescription = [
                "Gems contain special powers that can be used in battle",
                "Get gems from the gacha using gold or gacha tokens",
                "When you gain 3 of the same gem, it will level up to LV2"
                "When you gain 6 of the same gem, it will level up to LV3"
                "View and equip up to six gems from the [Equip gems] menu",
                "Select an equipped gem to unequip it",
                "In battle, activate gems from the [gems] menu",
                "Two gems must be activated at a time",
                "Each gem has an effect when activated, lasting until a different gem is selected",
                "If your two gems are a [best match], a bonus effect is applied"
            ]
            for string in gemDescription:
                print(string)
            input()
        elif menuInput == 4:
            equipRun = False
