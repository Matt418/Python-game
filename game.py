###Matt Gonzalez###
###Grant Tong###
###Period 4###

HERO_HEALTH = 100
MONSTER_HEALTH = 50


print("""You've'st'er'nd awaken in a dank cave that has a strange resemblance of a
Zelda dungeon. After walking for a while you stumble upon a large brass key
sitting in a mahogony chair. As you start to reach for the key, you are thrown
accross the room and land hard on the floor next to a pile of bones. Inside
the pile you find a mysterious object\n""")

weapon = input("Choose your weapon: ")

def damage_dealt():
    number = random.randint(0, 20)
    new_health = number - MONSTER_HEALTH

def damage_taken():
    number = random.randint(0, 20)
    new_health = number - HERO_HEALTH

print("""As you raise your""", weapon,""",you finally get a good look
at the monster. It is none other than Ronald McDonald weilding a
glowing broadsword made from french fries.""")
