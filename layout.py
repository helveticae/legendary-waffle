import random
import math

# Exempel på layout som BORDE funka i terminalen

#############################################################
#   
#   [P1_NAME]
#   [P1_COIN_AMMOUNT]
#   [P1_HP][P1_EQUIP]
#
#
#   [BATTLE_ARRAY_P1]
#
#   [BATTLE_ARRAY_P2]
#                               
#   [P2_NAME]
#   [P2_COIN_AMMOUNT]
#   [P2_HP][P2_EQUIP]
#   
#############################################################

Player_List = ["Player A", "Player B", "Ash", "Red"]

Item_List = ["Garden Gloves", "Lucky Amulet", "Wheel of Brie"]
Item_Desc = ["GRASS TYPE MON HAS +2 HP REGEN/SECOND", "50% CHANCE TO GET 1 COIN FOR EVERY KILL", "NORMAL TYPE MON HAS ATTACK + 1"]

class Item:
    def __init__(self, desc):
        self.desc = desc


class pokemon:
    def __init__(self, name, hv, level, HP, ATK, SPD, TYP):
        self.name = name
        self.hv = hv
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.TYP = SPD
        self.TYP = TYP

def get_HP(hv, level, HP):
   return math.ceil(HP * (1.5*2 + hv * level/100) + level + 10)

def get_Value(Value):
    return Value

def get_Level(level):
    if level <= 9:
        return (f" {level}")
    else:
        return level


a = random.randint(1,16)
i = random.randint(1,100)
z = random.randint(1,32)
b = random.randint(1,32)
s = random.randint(1,32)

P001 = pokemon(name="Bulbasaur", hv=a,level = 10, HP = z+2, ATK = b+1, SPD = s, TYP = "Grass")
P002 = pokemon(name="Ivysaur", hv=a,level = 12, HP = z+2, ATK = b+1, SPD = s, TYP = "Grass")
P003 = pokemon(name="Venusaur", hv=a,level = 10, HP = z+2, ATK = b+1, SPD = s, TYP = "Grass")
P172 = pokemon(name="Pichu", hv=a,level = i, HP = z, ATK = b, SPD = s, TYP = "Electric")
P025 = pokemon(name="Pikachu", hv=a,level = i, HP = z, ATK = b, SPD = s, TYP = "Electric")
P026 = pokemon(name="Raichu", hv=a,level = i, HP = z, ATK = b, SPD = s, TYP = "Electric")
P065 = pokemon(name="Alakazam", hv=a,level = 10, HP = z+2, ATK = b+1, SPD = s, TYP = "Psychic")
P107 = pokemon(name="Hitmonchan", hv=a,level = 10, HP = z, ATK = b+3, SPD = s, TYP = "Fighting")
P129 = pokemon(name="Toggepi", hv=0.1,level = 1, HP = -1, ATK = b+3, SPD = s, TYP = "Fighting")

PokeList = [P001, P002, P003, P172, P025, P026, P065, P107, P129]


P1_NAME = Player_List[0]
P1_COIN_AMMOUNT = 12
P1_HP = 20
P1_COIN = 10

random_item_p1 = random.randint(0,2)
P1_EQUIP = Item_List[random_item_p1]
P1_EQUIP_DESC = Item_Desc[random_item_p1]

#AMS = Active Mon Slot
P1AMS_1 = PokeList[random.randint(0,8)]
P1AMS_2 = P002
P1AMS_3 = P003

P2AMS_1 = P172
P2AMS_2 = P025
P2AMS_3 = P026

def B_ARRAY_STAT_P1():
    mon_1_length = get_HP(P1AMS_1.hv, P1AMS_1.level, P1AMS_1.HP)
    mon_2_length = get_HP(P1AMS_2.hv, P1AMS_2.level, P1AMS_1.HP)
    mon1 = len(str(mon_1_length))
    mon2 = len(str(mon_2_length))
    if mon1 == 1:
        b = -1
    if mon1 == 2:
        b = 1
    if mon1 == 3:
        b = 2
    if mon1 == 4:
        b = 3
    if mon2 == 1:
        a = 2
    elif mon2 == 2:
        a = 1
    elif mon2 == 3:
        a = 1
    elif mon2 == 4:
        a = 0
    SPACE1 = (6 - b + a) * (" ")


    SPACE2 = (16-(len(P1AMS_1.name))) * (" ")
    print(f"#    ", end='')
    print(f"{get_HP(P1AMS_1.hv, P1AMS_1.level, P1AMS_1.HP)} HP lv{get_Level(P1AMS_1.level)}{SPACE1}{get_HP(P1AMS_2.hv, P1AMS_2.level, P1AMS_2.HP)} HP lv{get_Level(P1AMS_2.level)} ")
    print(f"#    ", end='')
    print(f"{get_Value(P1AMS_1.name)}{SPACE2}{get_Value(P1AMS_2.name)}")

def B_ARRAY_STAT_P2():
    mon_1_length = get_HP(P2AMS_1.hv, P2AMS_1.level, P2AMS_1.HP)
    mon_2_length = get_HP(P2AMS_2.hv, P2AMS_2.level, P2AMS_1.HP)
    mon1 = len(str(mon_1_length))
    mon2 = len(str(mon_2_length))
    if mon1 == 1:
        b = -1
    if mon1 == 2:
        b = 1
    if mon1 == 3:
        b = 2
    if mon1 == 4:
        b = 3
    if mon2 == 1:
        a = 2
    elif mon2 == 2:
        a = 1
    elif mon2 == 3:
        a = 1
    elif mon2 == 4:
        a = 0
    SPACE1 = (6 - b + a) * (" ")


    SPACE2 = (16-(len(P2AMS_1.name))) * (" ")
    
    print(f"#    ", end='')
    print(f"{get_HP(P2AMS_1.hv, P2AMS_1.level, P2AMS_1.HP)} HP lv{get_Level(P2AMS_1.level)}{SPACE1}{get_HP(P2AMS_2.hv, P2AMS_2.level, P2AMS_2.HP)} HP lv{get_Level(P1AMS_2.level)} ")
    print(f"#    ", end='')
    print(f"{get_Value(P2AMS_1.name)}{SPACE2}{get_Value(P2AMS_2.name)}")

                       
P2_NAME = Player_List[1]
P2_COIN_AMMOUNT = 12
P2_HP = 20
P2_COIN = 10

random_item_p2 = random.randint(0,2)
P2_EQUIP = Item_List[random_item_p2]
P2_EQUIP_DESC = Item_Desc[random_item_p2]

b_title = " BATTLE MODE "

def render_border():
    print("#" * 24 + b_title + "#" * 24)
    print("#")
    print(f"#    {P1_NAME}")
    print(f"#    COIN: {P1_COIN}")
    print(f"#    HP: {P1_HP} / 20   {P1_EQUIP} ({P1_EQUIP_DESC})")
    print("#")
    B_ARRAY_STAT_P1()
    print("#")
    B_ARRAY_STAT_P2()
    print("#")
    print(f"#    {P2_NAME}")
    print(f"#    COIN: {P2_COIN}")
    print(f"#    HP: {P2_HP} / 20   {P2_EQUIP} ({P2_EQUIP_DESC})")
    print("#")
    print("#" * 24 + b_title + "#" * 24)

render_border()






######################## EXAMPLE ##############################
# 
#   PLAYER A
#   COIN: 10
#   HP: 20/20   GARDEN GLOVES (GRASS TYPE MON HAS +2 HP REGEN/SECOND)
#
#   (001 / 001)     (033 / 033)     (166 / 166)
#   [BULBASAUR]     [ IVYSAUR ]     [VENUSAUR ] 
#
#
#
#   [  PICHU  ]     [ PIKACHU ]     [ RAICHU  ]
#   (001 / 001)     (033 / 033)     (166 / 166)
# 
#   PLAYER B
#   COIN: 8
#   HP: 20/20   LUCKY AMULET (50% CHANCE TO GET 1 COIN FOR EVERY KILL)
#
# 
# 
################################################################
#   
#
#   [BUY_ARRAY]
#
#
#   [BATTLE_ARRAY]
#
#
#
#   [--------CURRENT_HAND--------]              [Player_Name]
#   [HP][EQUIP_SLOT][COIN_AMMOUNT]              [STATS]
#
#
#
#
#
