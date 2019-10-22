from Functions import *
import time

def gachaPull(player):
    allNameString = ["rabbit", "tank", "gorilla", "diamond", "hawk", "gatling", "ninja", "comic", "dragon", "lock"]
    timeout = 1
    timeout_start = time.time()

    def check_upgrade(gem):
        if gem == 3:
            return 2
        if gem == 6:
            return 3
        else:
            return 0

    # things got funky with lists so i give up on using a for loop with them
    # update: ya idk what's going on we're going full bulky code cuz things don't work
    addedGem = False
    while addedGem == False and time.time() < timeout_start + timeout:
        randomGem = (random.choice(allNameString))
        if randomGem == "rabbit":
            if player.rabbit == 6:
                pass
            elif player.rabbit < 6:
                player.rabbit += 1
                upgradeCheck = check_upgrade(player.rabbit)
                if upgradeCheck > 1 and player.rabbitEquip >= 1:
                    player.rabbitEquip = upgradeCheck
                addedGem = True
        elif randomGem == "tank":
            if player.tank == 6:
                pass
            elif player.tank < 6:
                player.tank += 1
                upgradeCheck = check_upgrade(player.tank)
                if upgradeCheck > 1 and player.tankEquip >= 1:
                    player.tankEquip = upgradeCheck
                addedGem = True
        elif randomGem == "gorilla":
            if player.gorilla == 6:
                pass
            elif player.gorilla < 6:
                player.gorilla += 1
                upgradeCheck = check_upgrade(player.gorilla)
                if upgradeCheck > 1 and player.gorillaEquip >= 1:
                    player.gorillaEquip = upgradeCheck
                addedGem = True
        elif randomGem == "diamond":
            if player.diamond == 6:
                pass
            elif player.diamond < 6:
                player.diamond += 1
                upgradeCheck = check_upgrade(player.diamond)
                if upgradeCheck > 1 and player.diamondEquip >= 1:
                    player.diamondEquip = upgradeCheck
                addedGem = True
        elif randomGem == "hawk":
            if player.hawk == 6:
                pass
            elif player.hawk < 6:
                player.hawk += 1
                upgradeCheck = check_upgrade(player.hawk)
                if upgradeCheck > 1 and player.hawkEquip >= 1:
                    player.hawkEquip = upgradeCheck
                addedGem = True
        elif randomGem == "gatling":
            if player.gatling == 6:
                pass
            elif player.gatling < 6:
                player.gatling += 1
                upgradeCheck = check_upgrade(player.gatling)
                if upgradeCheck > 1 and player.gatlingEquip >= 1:
                    player.gatlingEquip = upgradeCheck
                addedGem = True
        elif randomGem == "ninja":
            if player.ninja == 6:
                pass
            elif player.ninja < 6:
                player.ninja += 1
                upgradeCheck = check_upgrade(player.ninja)
                if upgradeCheck > 1 and player.ninjaEquip >= 1:
                    player.ninjaEquip = upgradeCheck
                addedGem = True
        elif randomGem == "comic":
            if player.comic == 6:
                pass
            elif player.comic < 6:
                player.comic += 1
                upgradeCheck = check_upgrade(player.comic)
                if upgradeCheck > 1 and player.comicEquip >= 1:
                    player.comicEquip = upgradeCheck
                addedGem = True
        elif randomGem == "dragon":
            if player.dragon == 6:
                pass
            elif player.dragon < 6:
                player.dragon += 1
                upgradeCheck = check_upgrade(player.dragon)
                if upgradeCheck > 1 and player.dragonEquip >= 1:
                    player.dragonEquip = upgradeCheck
                addedGem = True
        elif randomGem == "lock":
            if player.lock == 6:
                pass
            elif player.lock < 6:
                player.lock += 1
                upgradeCheck = check_upgrade(player.lock)
                if upgradeCheck > 1 and player.lockEquip >= 1:
                    player.lockEquip = upgradeCheck
                addedGem = True

    if addedGem == False:
        input("You already own all gems")

    if addedGem == True:
        input("...")
        input("...")
        input("...!")
        input("You got a {} gem!".format(randomGem))
        if upgradeCheck == 2:
            input("{} gem has been upgraded to LV2!".format(randomGem))
        elif upgradeCheck == 3:
            input("{} gem has been upgraded to LV3! (MAX)".format(randomGem))


def gachaMenu(player):
    gachaMenuList = ["Play gacha (100g)", "Play gacha (1 Gacha Token)", "Back"]

    gachaLoop = True
    while gachaLoop == True:
        print("Welcome to gacha")
        print("Gold: {} Tokens: {}".format(player.gold, player.gachaToken))
        print_list(gachaMenuList)
        gachaMenuInput = integer_input(len(gachaMenuList))

        if gachaMenuInput == 1:
            if player.gold >= 100:
                player.gold -= 100
                gachaPull(player)
            elif player.gold < 100:
                input("You don't have enough gold!")
            pass
        if gachaMenuInput == 2:
            if player.gachaToken >= 1:
                player.gachaToken -= 1
                gachaPull(player)
            elif player.gachaToken < 1:
                input("You have no gacha tokens!")
            pass
        if gachaMenuInput == 3:
            gachaLoop = False
