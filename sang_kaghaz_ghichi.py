import random
game_item = ['sang', 'kaghaz', 'gheichi']
print("khosh amdi be game")
print("_" * 20)
while True:
    print(f"1)sang\n2)kaghaz\n3)gheichi\n0)exit")
    choice = input("kodom ro entekhab mikoni: ")
    target = random.choice(game_item)
    print(f"your choice is : {choice}")
    print("_" * 20)
    bot = f"bot choice :{target}"
    match choice:
        case "1":
            print(bot)
            if target == "sang":
                print("mosavi shod")
            elif target == "kaghaz":
                print("shoma barande shodid")
            elif target == "gheichi":
                print("shoma bakhtid")
            else:
                print("wrong choice")
            print("_" * 20)
        case "2":
            print(bot)
            if target == "sang":
                print("shoma bordid")
            elif target == "kaghaz":
                print("mosavi shod")
            elif target == "gheichi":
                print("shoma bakhtid")
            else:
                print("wrong choice")
            print("_" * 20)
        case "3":
            print(bot)
            if target == "sang":
                print("shoma bakhtid")
            elif target == "kaghaz":
                print("shoma bordid")
            elif target == "gheichi":
                print("mosavi shod")
            else:
                print("wrong choice")
            print("_" * 20)
        case "0":
            leave = input("Do you want to exit? (y/n) ")
            if leave == "y":
                print("game end")
                break
            else:
                continue
        case _:
            print("Error: invalid number")
            continue

