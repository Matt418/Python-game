###Matt Gonzalez###
###Grant Tong###
###Period 4###

HERO_HEALTH = 100
MONSTER_HEALTH = 50

def main():
print("""You've'st'er'nd awaken in a dank cave that has a strange resemblance of a
Zelda dungeon. After walking for a while you stumble upon a large brass key
sitting in a mahogony chair. As you start to reach for the key, you are thrown
accross the room and land hard on the floor next to a pile of bones. Inside
the pile you find a mysterious object\n""")

weapon = input("Choose your weapon: ")

print("""\nAs you raise your""", weapon,""",you finally get a good look
at the monster. It is none other than Ronald McDonald: Guardian of all
chairs and keys, weilding a glowing broadsword made from french fries.
He gives you an evil grin as he charges towards you.""")
damage_dealt():
fifa_sequence()
def fifa_sequence():
    print("""You attacked first! You dealt""", number1,"""damage and the monster now
    has""", new_health1,""" Before you could follow up with another attack,""")
    print("""the monster strikes at you! You took""", number2,"""damage and your
current health is now""", new_health2)

def damage_dealt():
    number1 = random.randint(0, 20)
    if number == 0:
       damage_taken()
    else:
       new_health1 = number - MONSTER_HEALTH

def damage_taken():
    number2 = random.randint(0, 20)
    new_health2 = number - HERO_HEALTH
    

if MONSTER_HEALTH <0:
fifa_sequence()
    
else:
    print("""You've defeated the monster!""")


if HERO_HEALTH <0:
    print("""GIT GUD NUB """)
    damage_dealt()
    damage_taken()
    

