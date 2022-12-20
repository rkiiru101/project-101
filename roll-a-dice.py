import random

response = "y"

while response == "y":
    num = random.randint(1,3)
    if num == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif num == 2:
        print("[-----]")
        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print("[-----]")
    elif num == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        
    response = input("press y to roll again and n to exit: ")
    print('\n')