import random
import time
# Simple countdown
def countdown():
    time.sleep(2.5)
# Level up system
def Levelup():
    # logic for level up
    if player["Exp"] >= 100 * player["Level"]:
               up = player["Level"] + 1
               player["Level"] = up
               print("Player level up!")
               print("1. Health")
               print("2. Attack")
               print("3. Magic")
               print("4. Defense")
               up_Choice = int(input("What do you want to up?: "))
               # logic for up stats
               while True:
                match up_Choice:
                        case 1:
                            Hp_up = player["Hp"] + 30
                            player["Hp"] = Hp_up
                            break
                        case 2:
                            Attack_up = player["Attack"] + 10
                            player["Attack"] = Attack_up
                            break
                        case 3:
                            Magic_up = player["Magic"] + 1
                            player["Magic"] = Magic_up
                            break
                        case 4:
                            Defense_up = player["Defense"] + 1.5
                            player["Defense"] = Defense_up
                            break
                        case _:
                            print("Opção invalida")
               countdown()
               playerStatus(player)
# Monster creation
def create_monster():
    nome = "Monster"
    Hp = random.randint(1, 100)
    Attack = random.randint(1, 100)
    Exp = random.randint(1, 100)
    
            
    # Monster dictionary
    Monster = {"Name": nome,
               "Hp": Hp,
               "Attack": Attack,
               "Exp": Exp
    }
    return Monster
# Player attack system
def attack_System(player, monster):
    # logic for attack
    print("You try to attack the monster")
    pAttack = player["Attack"]
    mLife = monster["Hp"]
    result = mLife - pAttack
    monster["Hp"] = result
# Player defense system
def defense_System(player, monster):
    # logic for defense
    if choice == 2:
        Damage_defense = player["Hp"] - (monster["Attack"] - player["Defense"])
        player["Hp"] = Damage_defense
# Player magic system
def magic_System(player):
    if player["Magic"] == 10:
       health_magic = player["Hp"] + 50
# Monster attack system 
def monster_Attack(monster, player):
    M_Attack = random.randint(1,3)
    # If player choose defense
    if M_Attack == 2:
        print(f"The monster attack you!  monster attack: {monster['Attack']}")
        Damage = player["Hp"] - monster["Attack"]
        player["Hp"] = Damage
# Player types
def typesP(choice): #P = Player
    print("Choose your player:")
    print("1.Witcher")
    print("2.Warrior")
    print("3.Thief")
    print("4.Evil")
# Monster status
def monsterStatus(monster):
    print(f"Name: {monster["Name"]}")
    print(f"Hp: {monster["Hp"]}")
    print(f"Attack: {monster["Attack"]}")
    print(f"Exp: {monster["Exp"]}")
# Player status
def playerStatus(player):
    print(f"Name: {player["Name"]}")
    print(f"Hp: {player["Hp"]}")
    print(f"Attack: {player["Attack"]}")
    print(f"Level: {player["Level"]}")
    print(f"Exp: {player["Exp"]}")
    print(f"Magic: {player["Magic"]}")
# Player creation
def character(x):
    # logic for player creation
    while True:
        match x:
            case 1:
                Witch = {"Name": "Witch",
                    "Hp": 100,
                    "Attack": 10,
                    "Level": 1,
                    "Defense": 0,
                    "Exp": 0,
                    "Magic": 0}
                return Witch
                break
            case 2: 
                Warrior = {"Name": "Warrior",
                        "Hp": 100,
                        "Attack": 10,
                        "Level": 1,
                        "Defense": 0,
                        "Exp": 0,
                        "Magic": 0}
                return Warrior
                break
            case 3: 
                Thief = {"Name": "Thief",
                        "Hp": 100,
                        "Attack": 10,
                        "Level": 1,
                        "Defense": 0,
                        "Exp": 0,
                        "Magic": 0}
                return Thief
                break
            case 4:
                Evil = {"Name": "Evil",
                    "Hp": 100,
                    "Attack": 10,
                    "Level": 1,
                    "Defense": 0,
                    "Exp": 0,
                    "Magic": 0}
                return Evil
                break
            case _:
                print("Opção invalida")
# Menu game       
def menuGame():
    print("Choose your action")
    print("1.Attack")
    print("2.Defense")
    print("3.Magic")
    print("4.Exit")
    print("5.View your status")
    print("6.View monster status")

# Main game
choice = int(input("What's your choice?: "))
player = character(choice)
monster = create_monster()
monsterStatus(monster)
while True:
    
    
                
    menuGame()
    option = int(input("What do you want?: "))
    match option:
            case 1:
                print("You attack the monster")
            case 2:
                print("You try to defense monster attack")
                defense_System()
            case 3:
                if player["Magic"] <= 5:
                    print("You need level for this")
            case 4: 
                print("Thanks for play!!")
                break
            case 5: 
                playerStatus(player)
            case 6: 
                monsterStatus(monster)
            case _:
                print("Opção invalida")
            
    if option == 1:
        attack_System(player, monster)
        countdown()
        if monster["Hp"] <= 0:
           mExp = monster["Exp"]
           pExp = player["Exp"]
           player["Exp"]= pExp + mExp
           print("You defeat the monster!")
           Levelup()
           countdown()
           monster = create_monster()
           monsterStatus(monster)
        else:
            print(f"Hp: {monster["Hp"]}")
            print("Try one more time!!")
            monster_Attack(monster, player)
            countdown()
        if player["Hp"] == 0:
            print("You Died!")
            break
            
                
           