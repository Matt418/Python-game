###Matt Gonzalez###
###Grant Tong###
###Period 4###
import random


def main():
    print("""You've'st'er'nd awaken in a dank cave that has a strange resemblance of a
    Zelda dungeon. After walking for a while you stumble upon a large brass key
    sitting in a mahogony chair. As you start to reach for the key, you are
    thrown accross the room and land hard on the floor next to a pile of bones.
    Inside the pile you find a mysterious object\n""")

    weapon = input("Choose your weapon: ")

    print("""\nAs you raise your""", weapon,""",you finally get a good look
    at the monster. It is none other than Ronald McDonald: Guardian of all
    chairs and keys, weilding a glowing broadsword made from french fries.
    He gives you an evil grin as he charges towards you.""")
    choice1 = float(input("\nDo you 1. attack? or do you 2. run? (Enter ony the number one or the number two. EX: 1 or 2 if you add anything else, the game will crash): "))

    if choice1 == 1:
        retry = input("\nIt was a glorious battle but in the end, you were McMurdered by the evil clown. You have died. Try again? y/n:")
        if retry == 'y':
            main()
        else:
            quit()
    else:
        print("""\nYou escape with your life, barely escaping the grasp of Ronald
    Mcdonald. He shrieks as you steal the key and run for the door. After, you take the stairs beyond the dungeon,
    and find a two doors. The door on the left is old and rotten, behind it the screams of lost souls, while the
    other illuminates brightly, held together by golden hinges. Like a reasonable person, you pick the door on the left.
    To open the chest, you use your""", weapon ,""" you are shocked to see a treasure chest, filled with goblets, neckclaces,and jewels.""")
        def treasure_reward():
            amount = random.randint(0,150)
            print('You got',amount,'of items of the stash!')


        treasure_reward()
            

main()
