# Snake , Water , Gun Game

import random

def Game_Result(comp , player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'g':
        if player == 'w':
            return True
        elif player == 's' :
            return False
        elif comp == 'w':
            if player == 's':
                return True
            elif player == 'g':
                return False
      
        

print("computer's turn : Snake(s), Water(w) or Gun(g)")
no = random.randint(1,3)
if no==1:
    comp = 's'
elif no==2:
    comp = 'w'
elif no==3:
    comp = 'g'
player = input("player's turn: Snake(s) , Water(w) or Gun(g)")
a = Game_Result(comp,player)
print(f"comp choose {comp}")
print(f"you choose {player}")

if a == None:
    print("the game is a tie!")
elif a :
    print("you win!")
elif a :
    print("you lose!")
    