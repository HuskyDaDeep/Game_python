import random
import time

def countdown():
    time.sleep(2.5)

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
def typesP(): #P = Player
    print("Choose your player:")
    print("1.Witch")
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
                    "Attack": 1000,
                    "Level": 1,
                    "Exp": 0,
                    "Magic": 0}
                return Witch
            case 2: 
                Warrior = {"Name": "Warrior",
                        "Hp": 100,
                        "Attack": 10,
                        "Level": 1,
                        "Exp": 0,
                        "Magic": 0}
                return Warrior
            case 3: 
                Thief = {"Name": "Thief",
                        "Hp": 100,
                        "Attack": 10,
                        "Level": 1,
                        "Exp": 0,
                        "Magic": 0}
                return Thief
            case 4:
                Evil = {"Name": "Evil",
                    "Hp": 100,
                    "Attack": 10,
                    "Level": 1,
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
            case 3:
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
           if player["Exp"] >= 100 * player["Level"]:
               up = player["Level"] + 1
               player["Level"] = up
               print("Player level up!")
               countdown()
           countdown()
           monster = create_monster()
           monsterStatus()
        else:
            print(f"Hp: {monster["Hp"]}")
            print("Try one more time!!")
            countdown()