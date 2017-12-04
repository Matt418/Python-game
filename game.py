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


    choice1 = float(input("\nDo you 1. attack? or do you 2. run? (Enter ony the number one or the number two. EX: 1 or 2 if you add anything else,the game will crash: "))

    choice2= float(input("""\n Do you 1.attempt to jump
and open the gate, 2. or leave to another area of the castle?:\n""")
            if choice2 == 1;

                print("\n You jump over the pit, barely missing your footing to the other side. You crack open the gate with",weapon,"and finally escape the castle! Good job!")

            else:
                try_again = input("""\n you head into another room with several doors. However, it is not like any other room, as each door is a labyrith, taking you back to the
same room each time. Eventually you become insane and an undying keeper of doors, forever enslaved to the rooms. Want to try again?y/n:""")
                    if try_again== 'n':
                           main()
                    else:
                        quit()
        


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
    other illuminates brightly, held together by golden hinges. Like a reasonable person, you pick the door on the left. The room is filled with chest, all
    latched locked by iron locks. To open one of the chests, you use your""", weapon ,""" and shocked to find treasure  in the chest, filled with goblets,
    neckclaces,and jewels.""")
        def treasure_reward():
            amount = random.randint(0,150)
            print('You got',amount,'of items of the stash!')


            keep_going = input('\nDo you stay in hopes of finding more treasure from the chests, or take your reward and leave the room? yes/no:\n')

            if 'yes':
                    print("""You leave the room, and come across a gate. In front of it, there is a pit of snakes that reside a the bottom. do you 1.attempt to jump
and open the gate, 2. or leave to another area of the castle?:\n""")
            else:
                print("""Consumed by greed, you decide to stay and open all the chests,
finding treasure that filled your hearts desire. However, the cost for staying turned you
into a dragon,and hoarde the treasure for eternity!!!\n""")

                             
                
         treasure_reward()

    

    


        
            

main()
