from Functions import *
import random
from Gacha import *


class enemyType:
    def __init__(self, minHealth, maxHealth, minAttack, maxAttack, minGold, maxGold, name):
        self.minHealth = minHealth
        self.maxHealth = maxHealth
        self.minAttack = minAttack
        self.maxAttack = maxAttack
        self.minGold = minGold
        self.maxGold = maxGold
        self.name = name
        self.attackCharge = 0


class enemy:
    def __init__(self, enemyType):
        self.health = random.randint(enemyType.minHealth, enemyType.maxHealth)
        self.FullHealth = self.health  # most confusing variable names ever
        self.attack = random.randint(enemyType.minAttack, enemyType.maxAttack)
        self.FullAttack = self.attack  # wait why is this capitalized
        self.gold = random.randint(enemyType.minGold, enemyType.maxGold)
        self.name = enemyType.name
        self.attackCharge = enemyType.attackCharge


def new_enemy(enemyType):
    newEnemy = enemy(enemyType)
    return newEnemy


def command_select():
    print("(1) Attack")
    print("(2) Gems")
    print("(3) Item")
    command = integer_input(3)
    return command


def gemSlotAssign(name, equip, allEquippedGems):
    active = 0
    if equip > 0 and [name, equip, active] not in allEquippedGems:
        slot = [name, equip, active]
        return slot
    else:
        return []


def gemSlotAssignRepeater(player, allEquippedGems):
    allNameString = ["rabbit", "tank", "gorilla", "diamond", "hawk", "gatling", "ninja", "comic", "dragon", "lock"]
    allGemEquip = [player.rabbitEquip, player.tankEquip, player.gorillaEquip, player.diamondEquip, player.hawkEquip,
                   player.gatlingEquip, player.ninjaEquip, player.comicEquip, player.dragonEquip, player.lockEquip]


    for name, equip in zip(allNameString, allGemEquip):
        gemSlot = gemSlotAssign(name, equip, allEquippedGems)
        if gemSlot:
            return gemSlot


def gemsMenu(player, gemList, currentEnemy):
    # for some dumb reason unactivating gems is all the way up here god this is a mess
    # I guess I should've like used a seperate big function that contained all the stat stuff but it's too late for that

    # gem player buff effects
    LV1GEMHEAL = [1, 2]
    LV2GEMHEAL = [2, 4]
    LV3GEMHEAL = [4, 6]
    HEALLEVELS = [LV1GEMHEAL, LV2GEMHEAL, LV3GEMHEAL]
    LV1ATTACKRAISE = 2
    LV2ATTACKRAISE = 4
    LV3ATTACKRAISE = 6
    ATTACKRAISELEVELS = [LV1ATTACKRAISE, LV2ATTACKRAISE, LV3ATTACKRAISE]
    HEALINGGEMLIST = ["rabbit", "tank", "diamond", "ninja", "lock"]
    ATTACKGEMLIST = ["gorilla", "hawk", "gatling", "comic", "dragon"]
    RABBITTANK = ["rabbit", "tank"]
    GORILLADIAMOND = ["gorilla", "diamond"]
    HAWKGATALING = ["hawk", "gatling"]
    NINJACOMIC = ["ninja", "comic"]
    DRAGONLOCK = ["dragon", "lock"]
    BESTMATCHLIST = [RABBITTANK, GORILLADIAMOND, HAWKGATALING, NINJACOMIC, DRAGONLOCK]

    # this is exactly the same as the buff function below but im copy pasting it up here instead of reusing the one down there
    def debuff_level_select(gemIndex, debuffFunction, debuffAmounts):
        if gemList[gemIndex][2] == 1:
            debuffFunction(debuffAmounts[0])
        if gemList[gemIndex][2] == 2:
            debuffFunction(debuffAmounts[1])
        if gemList[gemIndex][2] == 3:
            debuffFunction(debuffAmounts[2])

    def attack_lower_player(attackLowerAmount):
        player.minAttack -= attackLowerAmount
        player.maxAttack -= attackLowerAmount
        print("(-{} attack)".format(attackLowerAmount))


    # unactivates gems
    def unactivateAllGems(gemList):
        print("Unactivating gems...")
        for x in range(len(gemList)):
            if gemList[x][2] > 0:
                # first we lower the stat, then unactivate
                gemName = gemList[x][0]
                if gemName in ATTACKGEMLIST:
                    debuff_level_select(x, attack_lower_player, ATTACKRAISELEVELS)
                gemList[x][2] = 0
        return gemList

    # cleans up gemList for use in print_list function, then displays gems
    gemPrintString = []
    for x in range(len(gemList)):
        # non equipped
        if gemList[x][2] == 0:
            if gemList[x][1] == 1:
                gemPrintString.append(gemList[x][0])
            elif gemList[x][1] == 2:
                gemPrintString.append(gemList[x][0] + " LV2")
            elif gemList[x][1] == 3:
                gemPrintString.append(gemList[x][0] + " LV3")
        # equipped
        elif gemList[x][2] > 0:
            if gemList[x][1] == 1:
                gemPrintString.append(gemList[x][0] + " (A)")
            elif gemList[x][1] == 2:
                gemPrintString.append(gemList[x][0] + " LV2 (A)")
            elif gemList[x][1] == 3:
                gemPrintString.append(gemList[x][0] + " LV3 (A)")
    gemPrintString.append("unactivate gems")
    gemPrintString.append("back")

    # gem input section
    gemInputLoop = True
    gem1Index = -1
    gem2Index = -1
    while gemInputLoop == True:
        # user inputs gem for slot 1
        print("Choose a gem for slot 1")
        print_list(gemPrintString)
        gem1Index = integer_input(len(gemPrintString)) - 1
        # this is the back button, it will skip enemy turn so it displays player command options again
        if gem1Index == len(gemPrintString) - 1:
            # this would trigger skip turn AND RESET ASSIGNED VALUES PLEASE (or maybe i don't have to)
            skipEnemyPhase = True
            return skipEnemyPhase
        # this is the unactivate gems button
        elif gem1Index == len(gemPrintString) - 2:
            gemList = unactivateAllGems(gemList)
            skipEnemyPhase = False
            return skipEnemyPhase
        # if gem is already activated, we ask again
        else:
            while gemList[gem1Index][2] > 0:
                print("Cannot activate gem that is already activated. Choose again", end="")
                gem1Index = integer_input(len(gemPrintString)) - 1
            # saves a copy of the old string in case if user chooses back
            gemPrintStringSave = gemPrintString[gem1Index]
            # adds the (a) to the string
            gemPrintString[gem1Index] = "{} (a)".format(gemPrintString[gem1Index])

        # user inputs gem for slot 2
        print("Choose a gem for slot 2")
        print_list(gemPrintString)
        gem2Index = integer_input(len(gemPrintString)) - 1
        # this is the back button, returns to first gem selection
        if gem2Index == len(gemPrintString) - 1:
            # resets first gem string to the save
            gemPrintString[gem1Index] = gemPrintStringSave
            # resets gem1Index to 0
            gem1Index = -1
        # this is the unactivate gems button
        elif gem2Index == len(gemPrintString) - 2:
            gemList = unactivateAllGems(gemList)
            skipEnemyPhase = False
            return skipEnemyPhase
        # if gem is already activated or is gem from 1st slot, we ask again
        else:
            while gemList[gem2Index][2] > 0 or gem2Index == gem1Index:
                print("Cannot activate gem that is already activated. Choose again", end="")
                gem2Index = integer_input(len(gemPrintString)) - 1

        # exits loop for input if both gems are valid
        if gem1Index >= 0 and gem2Index >= 0:
            gemInputLoop = False

    # unactivates all gems
    gemList = unactivateAllGems(gemList)

    # activates chosen gems
    print("Activating gems...")
    gemList[gem1Index][2] = gemList[gem1Index][1]
    gemList[gem2Index][2] = gemList[gem2Index][1]

    # runs corresponding heal/attack buff
    def buff_level_select(gemIndex, buffFunction, buffAmounts):
        if gemList[gemIndex][2] == 1:
            buffFunction(buffAmounts[0])
        if gemList[gemIndex][2] == 2:
            buffFunction(buffAmounts[1])
        if gemList[gemIndex][2] == 3:
            buffFunction(buffAmounts[2])

    # does the actual healing
    def heal_player(healRange):
        healAmount = random.randint(healRange[0], healRange[1])
        player.health += healAmount
        healAmount = prevent_overheal(player, healAmount)
        input("+{} health)".format(healAmount))

    # does the actual attack buff
    def attack_raise_player(attackRaiseAmount):
        player.minAttack += attackRaiseAmount
        player.maxAttack += attackRaiseAmount
        input("+{} attack)".format(attackRaiseAmount))

    # badly going through all the gems
    for gemIndex in gem1Index, gem2Index:
        gemName = gemList[gemIndex][0]
        print("{}! (".format(gemName.upper()), end="")
        if gemName in HEALINGGEMLIST:
            buff_level_select(gemIndex, heal_player, HEALLEVELS)
        if gemName in ATTACKGEMLIST:
            buff_level_select(gemIndex, attack_raise_player, ATTACKRAISELEVELS)


    def combined_gem_level():
        gem1Level = gemList[gem1Index][2]
        gem2Level = gemList[gem2Index][2]
        if gem1Level >= 1 and gem2Level >= 1:
            if gem1Level >= 2 and gem2Level >= 2:
                if gem1Level >= 3 and gem2Level >= 3:
                    return 3
                return 2
            return 1

    def rabbit_tank_effect(combinedGemLevel):
        def point_distributor(pointRange):
            healAmount = random.randint(pointRange[0], pointRange[1])
            attackAmount = (pointRange[2] - healAmount)
            player.health += healAmount
            healAmount = prevent_overheal(player, healAmount)
            currentEnemy.health -= attackAmount
            input("(effect: dealt {} damage, +{} health)".format(attackAmount, healAmount))

        if combinedGemLevel == 1:
            point_distributor([1, 2, 10])
        if combinedGemLevel == 2:
            point_distributor([3, 5, 20])
        if combinedGemLevel == 3:
            point_distributor([5, 7, 35])

    def gorilla_diamond_effect(combinedGemLevel):
        def lower_enemy_attack(lowerRate):
            if currentEnemy.attack / currentEnemy.FullAttack > 0.5:
                lowerAmount = round(currentEnemy.attack * lowerRate)
                if lowerAmount == 0:
                    lowerAmount = 1
                currentEnemy.attack -= lowerAmount
            else:
                lowerAmount = 0
            input("(effect: lowered enemy attack by {})".format(lowerAmount))

        if combinedGemLevel == 1:
            lower_enemy_attack(0.1)
        if combinedGemLevel == 2:
            lower_enemy_attack(0.2)
        if combinedGemLevel == 3:
            lower_enemy_attack(0.3)

    #damage is done down below
    def hawk_gatling_effect_charge(combinedGemLevel):
        if combinedGemLevel == 1:
            player.hawkGatlingCharge = [2, 5, 10]
        if combinedGemLevel == 2:
            player.hawkGatlingCharge = [2, 20, 25]
        if combinedGemLevel == 3:
            player.hawkGatlingCharge = [3, 25, 35]
        input("(effect: next {} attacks deal bonus damage)".format(player.hawkGatlingCharge[0]))

    def ninja_comic_effect(combinedGemLevel):
        def ham_point_distributor(pointRange):
            healAmount = random.randint(pointRange[0], pointRange[1])
            attackAmount = random.randint(pointRange[2], pointRange[3])
            player.health += healAmount
            healAmount = prevent_overheal(player, healAmount)
            currentEnemy.health -= attackAmount
            input("(effect: dealt {} damage, +{} health)".format(attackAmount, healAmount))

        if combinedGemLevel == 1:
            ham_point_distributor([0, 3, 0, 15])
        if combinedGemLevel == 2:
            ham_point_distributor([1, 5, 10, 30])
        if combinedGemLevel == 3:
            ham_point_distributor([3, 7, 20, 80])

    def dragon_lock_effect(combinedGemLevel):
        def dragon_vortex_finish(damageList, threshold):
            healthPercent = currentEnemy.health / currentEnemy.FullHealth
            if healthPercent >= threshold[0]:
                damage = damageList[0]
                currentEnemy.health -= damage
                input("(effect: dealt {} damage)".format(damage))
            elif healthPercent >= threshold[1]:
                damage = damageList[1]
                currentEnemy.health -= damage
                input("(effect: dealt {} damage)".format(damage))
            elif healthPercent >= threshold[2]:
                damage = damageList[2]
                currentEnemy.health -= damage
                input("(effect: dealt {} damage)".format(damage))
            else:
                currentEnemy.health = 0
                input("(effect: EXECUTE)")
                pass

        if combinedGemLevel == 1:
            dragon_vortex_finish([1, 8, 15], [0.7, 0.5, 0.2])
        if combinedGemLevel == 2:
            dragon_vortex_finish([5, 15, 30], [0.75, 0.55, 0.25])
        if combinedGemLevel == 3:
            dragon_vortex_finish([10, 30, 75], [0.8, 0.6, 0.3])


    # checks if best match
    gemName12 = [gemList[gem1Index][0], gemList[gem2Index][0]]
    gemName21 = [gemList[gem2Index][0], gemList[gem1Index][0]]
    if gemName12 in BESTMATCHLIST or gemName21 in BESTMATCHLIST:
        combinedGemLevel = combined_gem_level()
        if combinedGemLevel == 1:
            print("BEST MATCH! ", end="")
        elif combinedGemLevel == 2:
            print("SUPER BEST MATCH! ", end="")
        elif combinedGemLevel == 3:
            print("GENIUS BEST MATCH! ", end="")  # I don't know what it's actually supposed to say

        if gemName12 == RABBITTANK or gemName21 == RABBITTANK:
            rabbit_tank_effect(combinedGemLevel)
        if gemName12 == GORILLADIAMOND or gemName21 == GORILLADIAMOND:
            gorilla_diamond_effect(combinedGemLevel)
        if gemName12 == HAWKGATALING or gemName21 == HAWKGATALING:
            hawk_gatling_effect_charge(combinedGemLevel)
        if gemName12 == NINJACOMIC or gemName21 == NINJACOMIC:
            ninja_comic_effect(combinedGemLevel)
        if gemName12 == DRAGONLOCK or gemName21 == DRAGONLOCK:
            dragon_lock_effect(combinedGemLevel)


    skipEnemyPhase = False
    return skipEnemyPhase


def game(player):
    # initializing
    player.health = player.maxHealth
    goldThisRun = 0
    if player.healthPotion > 5:
        player.carryHealthPotion = 5
    else:
        player.carryHealthPotion = player.healthPotion
    if player.maxHealthPotion > 5:
        player.carryMaxHealthPotion = 5
    else:
        player.carryMaxHealthPotion = player.maxHealthPotion

    # sets up enemies
    forestEnemy = enemyType(5, 10, 2, 3, 5, 10, "Snake")
    forestBoss = enemyType(25, 25, 5, 5, 75, 75, "COBRA")
    caveEnemy = enemyType(25, 35, 4, 7, 10, 20, "Small Bat")
    caveBoss = enemyType(100, 100, 12, 12, 250, 250, "GIANT BAT")
    swampEnemy = enemyType(80, 100, 10, 15, 50, 70, "Lizard")
    swampBoss = enemyType(300, 300, 20, 20, 700, 700, "CROCODILE")
    iceLandsBoss1 = enemyType(1000, 1000, 25, 25, 0, 0, "ICE BIRD")
    iceLandsBoss2 = enemyType(1000, 1000, 0, 0, 0, 0, "EGG")
    iceLandsBoss3 = enemyType(600, 600, 25, 25, 5000, 5000, "ICE BIRD (REVIVE)")


    # gem initializing, makes list of all equipped gems
    allEquippedGems = []
    gemSlot1 = []
    gemSlot2 = []
    gemSlot3 = []
    gemSlot4 = []
    gemSlot5 = []
    gemSlot6 = []

    # assigns equipped gems to gem slots
    for gemSlot in gemSlot1, gemSlot2, gemSlot3, gemSlot4, gemSlot5, gemSlot6:
        gemSlot = gemSlotAssignRepeater(player, allEquippedGems)
        allEquippedGems.append(gemSlot)
    # removes empty slots
    allEquippedGems = list(filter(None, allEquippedGems))

    def fighting_enemy_phase():
        # for some reason health pot values are here
        HEALTHPOTIONHEALAMOUNT = 50
        eggCharge = 0

        #boss attacks and hawk gatling
        def hawk_gatling_effect_damage():
            player.hawkGatlingCharge[0] -= 1
            damage = random.randint(player.hawkGatlingCharge[1], player.hawkGatlingCharge[2])
            currentEnemy.health -= damage
            print("Hawk Gatling DMG: {}" .format(damage))

        def boss_heal(healRange):
            healAmount = random.randint(healRange[0], healRange[1])
            currentEnemy.health += healAmount
            print("{} healed for {} health".format(currentEnemy.name, healAmount))
            print()

        def boss_attack_buff(buffRange):
            buffAmount = random.randint(buffRange[0], buffRange[1])
            currentEnemy.attack += buffAmount
            print("{} raised its attack by {}".format(currentEnemy.name, buffAmount))
            print()

        def boss_charge():
            print("{} seems to be charging a strong attack".format(currentEnemy.name))
            print()
            return 1

        def boss_icicle_charge():
            print("An icicle is coming! It will strike next turn!")
            print()
            return 2

        def boss_use_charge(flatDmg):
            #either does half of player's health, or a flat amount, whichever's higher (percent should always be higher unless if weird stuff happens)
            percentDmg = player.maxHealth//2
            if percentDmg > flatDmg and currentEnemy.name != "ICE BIRD (REVIVE)":
                player.health -= percentDmg
                print("Took {} damage!!".format(percentDmg))
                print()
            else:
                player.health -= percentDmg
                print("Took {} damage!!".format(flatDmg))
                print()
            return 0

        def boss_use_icicle_charge(dmg):
            player.health -= dmg
            print("The icicle does {} damage!" .format(dmg))
            return 0


        # loop runs until enemy or you are dead
        while currentEnemy.health > 0 and player.health > 0:
            skipEnemyPhase = False
            print("{}: {}\n{}: {}".format(player.name, player.health, currentEnemy.name, currentEnemy.health))
            command = command_select()
            # player phase
            if command == 1:
                damage = random.randint(player.minAttack, player.maxAttack)
                currentEnemy.health -= damage
                if player.hawkGatlingCharge[0] > 0:
                    hawk_gatling_effect_damage()
                print("Dealt {} damage!".format(damage))
            elif command == 2:
                skipEnemyPhase = gemsMenu(player, allEquippedGems, currentEnemy)
                # make skipTurn variable for when player chooses back to skip the enemy phase
            elif command == 3:
                print("(1) Health potion ({})".format(player.carryHealthPotion))
                print("(2) Max health potion ({})".format(player.carryMaxHealthPotion))
                if player.teleporter == 0:
                    print("(3) ???")
                if player.teleporter > 0:
                    print("(3) Use teleporter")
                print("(4) Quit")
                itemInput = integer_input(4)
                if itemInput == 1:
                    if player.carryHealthPotion > 0:
                        player.carryHealthPotion -= 1
                        player.healthPotion -= 1
                        player.health += HEALTHPOTIONHEALAMOUNT
                        healAmount = prevent_overheal(player, HEALTHPOTIONHEALAMOUNT)
                        input("Healed {} health".format(healAmount))
                    else:
                        input("You do not own this item")
                        skipEnemyPhase = True
                if itemInput == 2:
                    if player.carryMaxHealthPotion > 0:
                        player.carryMaxHealthPotion -= 1
                        player.maxHealthPotion -= 1
                        input("Healed {} health".format(player.maxHealth - player.health))
                        player.health = player.maxHealth
                    else:
                        input("You do not own this item")
                        skipEnemyPhase = True
                if itemInput == 3:
                    if player.glacialStorm == True:
                        player.glacialStorm = False
                        print("You teleport to safety")
                    elif player.teleporter == 0:
                        input("???")
                    elif player.teleporter > 0:
                        def teleporter_text():
                            input("You activate the teleporter")
                            input("...")
                            input("...")
                        teleporterList = ["Quit to main menu", "Skip to boss", "Back"]
                        print_list(teleporterList)
                        teleporterInput = integer_input(len(teleporterList))
                        if teleporterInput == 1:
                            teleporter_text()
                            input("...?")
                            input("But nothing happened")
                            input("!!")
                            input("-{} health!" .format(player.health))
                            player.health = 0
                            skipEnemyPhase = True
                        elif teleporterInput == 2:
                            if currentEnemy.name == forestEnemy.name and player.forestFirstClear == False:
                                teleporter_text()
                                player.skipStage = True
                                skipEnemyPhase = True
                                break
                            elif currentEnemy.name == caveEnemy.name and player.caveFirstClear == False:
                                teleporter_text()
                                player.skipStage = True
                                skipEnemyPhase = True
                                break
                            elif currentEnemy.name == swampEnemy.name and player.swampFirstClear == False:
                                teleporter_text()
                                player.skipStage = True
                                skipEnemyPhase = True
                                break
                            else:
                                teleporter_text()
                                input("But nothing happened")
                        if teleporterInput == 3:
                            skipEnemyPhase = True
                if itemInput == 4:
                    skipEnemyPhase = True

            #glacial storm phase
            if player.glacialStorm == True:
                player.health -= 10
                print("The glacial storm does 10 damage!")

            # enemy phase (skip if they dead or user did not make action)
            if currentEnemy.health <= 0:
                skipEnemyPhase = True
            if skipEnemyPhase == False:
                # if boss, has access to special attacks
                if currentEnemy.name == "GIANT BAT":
                    # 20% chance for boss to heal instead of attack when health is above 80%
                    rando = random.randint(1, 5)
                    if rando == 1 and currentEnemy.health/currentEnemy.FullHealth <= 0.8:
                        boss_heal([15, 20])
                    else:
                        player.health -= currentEnemy.attack
                        print("Took {} damage!".format(currentEnemy.attack))
                        print()
                elif currentEnemy.name == "CROCODILE":
                    # 20% chance to charge a large attack
                    # 10% chance to raise attack
                    rando = random.randint(1,10)
                    if currentEnemy.attackCharge == 1:
                        currentEnemy.attackCharge = boss_use_charge(40)
                    elif rando <= 2:
                        currentEnemy.attackCharge = boss_charge()
                    elif rando == 3:
                        boss_attack_buff([4, 6])
                    else:
                        player.health -= currentEnemy.attack
                        print("Took {} damage!".format(currentEnemy.attack))
                        print()
                elif currentEnemy.name == "ICE BIRD":
                    #70% attack
                    #20% heal for 70
                    #10% glacial storm
                    rando = random.randint(1,10)
                    if rando <= 1 and player.glacialStorm == False:
                        player.glacialStorm = True
                        print("ICE BIRD summons a glacial storm!")
                        input("(you can teleport out)")
                    elif rando <= 3:
                        boss_heal([60, 80])
                    else:
                        player.health -= currentEnemy.attack
                        print("Took {} damage!".format(currentEnemy.attack))
                        print()
                elif currentEnemy.name == "EGG":
                    #charges 10dmg per turn
                    eggCharge += 1
                    print("You feel a presence from inside the egg")
                    print()
                elif currentEnemy.name == "ICE BIRD (REVIVE)":
                    #60% attack
                    #10% heal
                    #10% large attack
                    #10% icicle
                    #10% glacial storm
                    rando = random.randint(1,10)
                    if currentEnemy.attackCharge == 2:
                        #icicle charge use. bird can still attack this turn
                        currentEnemy.attackCharge = boss_use_icicle_charge(30)
                    if currentEnemy.attackCharge == 1:
                        #large attack charge use. this counts as the attack
                        currentEnemy.attackCharge = boss_use_charge(60)
                    elif rando <= 1 and player.glacialStorm == False:
                        player.glacialStorm = True
                        print("ICE BIRD summons a glacial storm!")
                    elif rando <2:
                        boss_heal([60, 80])
                    elif rando <3:
                        currentEnemy.attackCharge = boss_charge()
                    elif rando <4:
                        currentEnemy.attackCharge = boss_icicle_charge()
                    else:
                        player.health -= currentEnemy.attack
                        print("Took {} damage!".format(currentEnemy.attack))
                        print()



                # for non-bosses
                else:
                    player.health -= currentEnemy.attack
                    print("Took {} damage!".format(currentEnemy.attack))
                    print()



        # enemy defeat
        if currentEnemy.health <= 0 and currentEnemy.name == "ICE BIRD":
            print("You defeated ICE BIRD")
            input("It seems to have turned into an egg")
            return "enemy dead"
        elif currentEnemy.health <= 0 and currentEnemy.name == "EGG":
            eggDamage = eggCharge * 10
            player.health -= eggDamage
            print("The egg bursts open!")
            input("Took {} damage!!!".format(eggDamage))
            return "enemy dead"
        elif currentEnemy.health <= 0:
            player.gold += currentEnemy.gold
            print("You defeated {}".format(currentEnemy.name))
            if player.health < player.maxHealth:
                player.health += player.regen
                print("Regenerated {} health".format(player.regen))
            input("Gained {} gold".format(currentEnemy.gold))
            return "enemy dead"
        # player defeat
        elif player.health <= 0:
            input("You are out of health and are forced to retreat")
            input("You have gained {} gold ({} total)".format(goldThisRun, player.gold))
            return "player dead"

    # FOREST
    print("You enter the forest")

    # forest normal enemies
    for loop in range(random.randint(10, 15)):
        round = loop + 1
        print("Forest level {}".format(round))
        currentEnemy = new_enemy(forestEnemy)

        # loops until player or enemy is dead
        exitCode = fighting_enemy_phase()
        # I have absolutely no idea why this isn't in the function
        if exitCode == "enemy dead":
            goldThisRun += currentEnemy.gold
            print()
        elif exitCode == "player dead":
            break
        if player.skipStage == True:
            player.skipStage = False
            break

    # forest boss
    if player.health > 0:
        currentEnemy = new_enemy(forestBoss)
        print_warning()
        print("Forest BOSS")
        exitCode = fighting_enemy_phase()
        if exitCode == "enemy dead":
            goldThisRun += currentEnemy.gold
            if player.forestFirstClear == True:
                player.rabbit += 1
                player.gachaToken += 1
                player.forestFirstClear = False
                input("You examine the body of the cobra...")
                input("You found a rabbit gem!")
                input("You found a gacha token!")
                input("The rabbit gem seems to hold special powers. Try equipping it in the [equip] menu")
                input("You can now use [gacha] from the shop")
            elif player.forestFirstClear == False:
                player.gachaToken += 1
                input("You examine the body of the cobra...")
                input("You found a gacha token!")
            print()
        elif exitCode == "player dead":
            pass

    # CAVE
    if player.health > 0:
        print("You continue into the cave")

        # cave normal enemies
        for loop in range(random.randint(10, 15)):
            round = loop + 1
            print("Cave level {}".format(round))
            currentEnemy = new_enemy(caveEnemy)

            # loops until player or enemy is dead
            exitCode = fighting_enemy_phase()
            if exitCode == "enemy dead":
                goldThisRun += currentEnemy.gold
                print()
            elif exitCode == "player dead":
                break
            if player.skipStage == True:
                player.skipStage = False
                break

        # cave boss
        if player.health > 0:
            currentEnemy = new_enemy(caveBoss)
            print_warning()
            print("Cave BOSS")
            exitCode = fighting_enemy_phase()
            if exitCode == "enemy dead":
                goldThisRun += currentEnemy.gold
                if player.caveFirstClear == True:
                    player.caveFirstClear = False
                    player.gachaToken += 3
                    player.teleporter = 1
                    input("You examine the body of the giant bat...")
                    input("You found 3 gacha tokens!")
                    input("You found a teleporter!")
                    input("With this, you can teleport back to the main menu at any time")
                    input("You can also skip straight to the boss of stages you've cleared previously")
                elif player.caveFirstClear == False:
                    caveBossDrop = random.randint(1,3)
                    player.gachaToken += caveBossDrop
                    input("You examine the body of the giant bat...")
                    input("You found {} gacha tokens!" .format(caveBossDrop))
                print()
            elif exitCode == "player dead":
                pass

    # SWAMP
    if player.health > 0:
        print("You continue into the swamp")

        # swamp normal enemies
        for loop in range(random.randint(10, 15)):
            round = loop + 1
            print("Swamp level {}".format(round))
            currentEnemy = new_enemy(swampEnemy)

            # loops until player or enemy is dead
            exitCode = fighting_enemy_phase()
            if exitCode == "enemy dead":
                goldThisRun += currentEnemy.gold
                print()
            elif exitCode == "player dead":
                break
            if player.skipStage == True:
                player.skipStage = False
                break

        # cave boss
        if player.health > 0:
            currentEnemy = new_enemy(swampBoss)
            print_warning()
            print("Swamp BOSS")
            exitCode = fighting_enemy_phase()
            if exitCode == "enemy dead":
                goldThisRun += currentEnemy.gold
                if player.swampFirstClear == True:
                    player.swampFirstClear = False
                    player.crocodileHeart = 1
                    player.maxHealth += 25
                    # if you update this please update it in the shop too
                    input("You examine the body of the crocodile...")
                    input("You found a crocodile heart!")
                    input("Your maximum health will be increased by 25")
                elif player.caveFirstClear == False:
                    crocodileExtraGold = random.randint(200, 300)
                    player.gold += crocodileExtraGold
                    input("You examine the body of the crocodile...")
                    input("You found {} extra gold!" .format(crocodileExtraGold))
                print()
            elif exitCode == "player dead":
                pass

    #ICE LANDS
    if player.health > 0:
        print("You continue into the ice lands")
        player.walled = False
        currentEnemy = new_enemy(iceLandsBoss1)
        print_warning()
        print("Ice Lands BOSS")
        exitCode = fighting_enemy_phase()
        if exitCode == "enemy dead":
            # bird phase 1 is dead
            currentEnemy = new_enemy(iceLandsBoss2)
            exitCode = fighting_enemy_phase()
            if exitCode == "enemy dead":
                # bird phase 2 is dead
                currentEnemy = new_enemy(iceLandsBoss3)
                exitCode = fighting_enemy_phase()
                if exitCode == "enemy dead":
                    # bird phase 3 is dead
                    input("yay you beat the game")
                pass
            print()
        elif exitCode == "player dead":
            pass
