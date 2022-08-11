import math
import random
import time

# Enkla funktioner för att lägga till och ta bort värde från x
def add_one_to_input(i):            # x+1
    return i + 1
def remove_one_from_input(i):       # x-1
    return i - 1
def multiply_self_once(i):          # x*x (square)
    return i * i
def double(i):                      # x*2
    return i * 2
def tripple(i):                     # x*3
    return i * 3
def multiply_self_twice(i):         # x*x*x (cube)
    return i * i * i
def split_even_once(i):             # x/2
    return i / 2

# Konverteringar & SI
def circumference_from_radius(i):   # Kalkylerar en cirkels omkrets från radie
    return (i * 2)*pi
def fahr_to_cel(i):                 # Konverterar Fahrenheit till Celcius
    i = (i - 32) / 1.8
    return i
def miles_to_kilo(i):               # Konverterar amerikanska miles till kilometer
    return i * 1.6
def mps_to_kmps(i):                 # Konverterar meter/sekund till kilometer/timme
    return i * 3.6
def kmps_to_mps(i):                 # Konverterar kilometer/timme till meter/sekund
    return i / 3.6

# Funktioner med två inputs
def add_to_i(i,a):                  # x+y
    return i + a
def remove_from_a(i,a):             # x-y
    return i - a
def multiply_by_a(i, a):            # x*y
    return i * a
def divide_by_a(i,a):               # x/y    
    try:
        return i / a 
    except:
        a = 0 
        print("Cannot divide by zero.")
def percentage_of_a(i,a):           # 100*i/a (Räknar procent/sannolikhet)
    return 100 * i / a
def pythagora(i,a):                 # x^2 + y^2 = z^2
    c = mul(i) + mul(a)
    return sqroot(c)

# Funktioner med tre inputs
def get_volume(i,a,b):              # x * y * z
    return i * a * b
def get_something(i,a,b):           # dags att skriva roligare saker
    start = i
    end = a
    steps = b

    return b / a-i

# Funktioner utan input
def coin_toss():                    # Returnerar 0 eller 1
    i = random.randint(0,1)
    return i
def return_four():                  # Returnerar fyra slumpade värden
    a = random.randint(1,16)
    i = random.randint(1,100)
    z = random.randint(1,32)
    b = random.randint(1,32)
    return a, i, z, b

# Variabelnamn
ad1 = add_one_to_input
rm1 = remove_one_from_input
mul = multiply_self_once
tri = tripple
Dub = double
mu2 = multiply_self_twice
spl = split_even_once

# Konvertering
circum = circumference_from_radius
ftoc = fahr_to_cel
mi2km = miles_to_kilo
ms2km = mps_to_kmps
lm2ms = kmps_to_mps

# Enkel matte med två inputs
addto = add_to_i
remfrom = remove_from_a
mulby = multiply_by_a
divby = divide_by_a
perof = percentage_of_a
vol = get_volume

# Mer matte med math-modulen
e = math.e      #  e = namn på variabel för Eulers tal (2,71828∞)
pi = math.pi    # pi = namn på variabel för Pi (3,14∞)


sqroot = math.sqrt                  # Returnerar roten av x

# Kvantifierar x (TYP conversions)
upp = math.ceil                     # Rundar x upp närmsta heltal (Ceiling)
flr = math.floor                    # Rundar x ner närmsta heltal (Flooring)
abs = math.fabs                     # Omvandlar till absolut värde (Negativa tal omvandlas till positiva) 
fac = math.factorial                # Returnerar fakultet 


# Validering
inf = math.isinf                    # Returnerar TRUE om talet är infinit (oändligt).
fin = math.isfinite                 # Returnerar TRUE om talet är finit (ändligt).
n4n = math.isnan                    # Returnerar TRUE om taler är nan (not a number)

class pokemon:
    def __init__(self, hv, level, HP, ATK, SPD, TYP):
        self.hv = hv
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.TYP = SPD
        self.TYP = TYP

    def getHP(self):
        return upp(self.HP * (1.5*e + self.hv * self.level/100) + self.level + 10)
    
    def getATK(self):
        return upp(self.ATK * (e + self.hv * self.level/100))

    def getLV(self):
        return self.level

    def newcreation(self, hv, level, HP, ATK):
        a = random.randint(1,16)
        i = random.randint(1,100)
        z = random.randint(1,32)
        b = random.randint(1,32)

a = random.randint(1,16)
i = random.randint(1,100)
z = random.randint(1,32)
b = random.randint(1,32)
s = random.randint(1,32)

Alakazam = pokemon(hv=a,level = 10, HP = z+2, ATK = b+1, SPD = s, TYP = "Psychic")
Hitmonchan = pokemon(hv=a,level = 10, HP = z, ATK = b+3, SPD = s, TYP = "Fighting")
Pikachu = pokemon(hv=a,level = i, HP = z, ATK = b, SPD = s, TYP = "Electric")


print(f"Pikachu har genererats, level {pokemon.getLV(Pikachu)}")
print(f"HP: {pokemon.getHP(Pikachu)}")


c = random.randint(0,2)

mylist2 = [Alakazam, Hitmonchan, Pikachu]

def get_HP(hv, level, HP):                                     # Works with class
   return upp(HP * (1.5*e + hv * level/100) + level + 10)

def get_ATK(hv, level, ATK):
    return upp(ATK * (e + hv * level/100))                      # Works with class

def remaining_HP(i,a):
    mon1 = i #(mon getting attacked)
    mon2 = a #(mon attacking)
    x, y, z = mon1[0], mon1[1], mon1[2] 
    a, b, c = mon2[0], mon2[1], mon2[3]
    remaining = get_HP(x,y,z) - get_ATK(a,b,c)
    #print(f"{i}, lost {a + b + c} HP")
    return remaining

def remaining_HP2(i,a):                     #TODO Change variables to self.var and move to class mon
    mon1 = i #(mon getting attacked)
    mon2 = a #(mon attacking)
    x, y, z = mon1[0], mon1[1], mon1[2] 
    a, b, c = mon2[0], mon2[1], mon2[3]
    remaining = get_HP(x,y,z) - get_ATK(a,b,c)
    #print(f"{i}, lost {a + b + c} HP")
    return remaining

def random_encounter():
        n = random.randint(1,3)
        print(n)



print(f"Himonchan: {get_HP(Hitmonchan.hv, Hitmonchan.level, Hitmonchan.HP)} HP")
print(f"Alakazam: {get_ATK(Alakazam.hv, Alakazam.level, Alakazam.ATK)} Attack")

testvar = get_HP(Hitmonchan.hv, Hitmonchan.level, Hitmonchan.HP) - get_ATK(Alakazam.hv, Alakazam.level, Alakazam.ATK)



print(testvar)

print(f"Himonchan: {get_HP(Hitmonchan.hv, Hitmonchan.level, Hitmonchan.HP)} HP")
print(f"Alakazam: {get_ATK(Alakazam.hv, Alakazam.level, Alakazam.ATK)} Attack")


# Exempel

# print(math.isinf(math.e)) # => FALSE
# print(inf(math.e)) # => FALSE
# print(math.isfinite(e)) #=> TRUE
# print(range(math.e))  # => object of TYP 'float' has no len
# Vi ser här att e redan har blivit kvantifierat 

################################################################
# 
# 
#
#
#
#
#
#
# mylist = [e, 2, 4]
# enkel_matte = [ad1, rm1, mul, tri, spl]
#
# len returnerar antal (längd/length) av objekt i en lista
# 
# li[0]
# li[start:end:step]
# li[::-1]
# 
#
# #p = 1666
# #print(sqroot(p))
# #print(mul(p))
# #print(math.cos(p))
# #print(math.cos(e))
# #print(remove_from_x(p,e))
# #
# #print(f"Procent: {percentage_of_y(100,p)}")
# #print(f"Delat med: {divide_by_y(100,p)}")
# #
# #print(ad1(2))
# #print(pythagora(5,12))
# print(circum(2))
##############################################################
