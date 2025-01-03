import random
import time

def countdown():
    time.sleep(2.5)
def Levelup():
    if player["Exp"] >= 100 * player["Level"]:
               up = player["Level"] + 1
               player["Level"] = up
               print("Player level up!")
               print("1. Health")
               print("2. Attack")
               print("3. Magic")
               print("4. Defense")
               up_Choice = int(input("O que deseja evoluir? "))
               
               match up_Choice:
                    case 1:
                        Hp_up = player["Hp"] + 30
                        player["Hp"] = Hp_up
                    case 2:
                        Attack_up = player["Attack"] + 10
                        player["Attack"] = Attack_up
                    case 3:
                        Magic_up = player["Magic"] + 1
                        player["Magic"] = Magic_up
                    case 4:
                        Defense_up = player["Defense"] + 1.5
                        player["Defense"] = Defense_up
               countdown()
def create_monster():
    nome = "Monster"
    Hp = random.randint(1, 100)
    Attack = random.randint(1, 100)
    Exp = random.randint(1, 100)
    
            
    
    Monster = {"Name": nome,
               "Hp": Hp,
               "Attack": Attack,
               "Exp": Exp
    }
    return Monster
def defense_System(): 
    if choice == 2:
        Damage_defense = player["Hp"] - (monster["Attack"] - player["Defense"])
        player["Hp"] = Damage_defense
def magic_System():
    a     
def monster_Attack():
    M_Attack = random.randint(1,3)
    if M_Attack == 2:
        print(f"The monster attack you!  monster attack: {monster['Attack']}")
        Damage = player["Hp"] - monster["Attack"]
        player["Hp"] = Damage
def typesP(): #P = Player
    print("Choose your player:")
    print("1.Witcher")
    print("2.Warrior")
    print("3.Thief")
    print("4.Evil")
def monsterStatus():
    print(f"Name: {monster["Name"]}")
    print(f"Hp: {monster["Hp"]}")
    print(f"Attack: {monster["Attack"]}")
    print(f"Exp: {monster["Exp"]}")
def playerStatus():
    print(f"Name: {player["Name"]}")
    print(f"Hp: {player["Hp"]}")
    print(f"Attack: {player["Attack"]}")
    print(f"Level: {player["Level"]}")
    print(f"Exp: {player["Exp"]}")
    print(f"Magic: {player["Magic"]}")
def character(x):
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
            case 2: 
                Warrior = {"Name": "Warrior",
                        "Hp": 100,
                        "Attack": 10,
                        "Level": 1,
                        "Defense": 0,
                        "Exp": 0,
                        "Magic": 0}
                return Warrior
            case 3: 
                Thief = {"Name": "Thief",
                        "Hp": 100,
                        "Attack": 10,
                        "Level": 1,
                        "Defense": 0,
                        "Exp": 0,
                        "Magic": 0}
                return Thief
            case 4:
                Evil = {"Name": "Evil",
                    "Hp": 100,
                    "Attack": 10,
                    "Level": 1,
                    "Defense": 0,
                    "Exp": 0,
                    "Magic": 0}
                return Evil
        
def menuGame():
    print("Choose your action")
    print("1.Attack")
    print("2.Defense")
    print("3.Magic")
    print("4.Exit")
    print("5.View your status")
    print("6.View monster status")


choice = int(input("What's your choice?: "))
player = character(choice)
monster = create_monster()
monsterStatus()
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
                playerStatus()
            case 6: 
                monsterStatus()
            case _:
                print("Opção invalida")
            
    if option == 1:
        print("You try to attack the monster")
        pAttack = player["Attack"]
        mLife = monster["Hp"]
        result = mLife - pAttack
        monster["Hp"] = result
        countdown()
        if monster["Hp"] <= 0:
           mExp = monster["Exp"]
           pExp = player["Exp"]
           player["Exp"]= pExp + mExp
           print("You defeat the monster!")
           Levelup()
           countdown()
           monster = create_monster()
           monsterStatus()
        else:
            print(f"Hp: {monster["Hp"]}")
            print("Try one more time!!")
            monster_Attack()
            countdown()
        if player["Hp"] == 0:
            print("You Died!")
            break
            
                
           