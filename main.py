from random import randint

# define option for game
options = ['rock', 'papers', 'scissors']

def Play():
    
    while True:
       computer_play=options[randint(0,3)]
       user_play=input("Enter a option among ('rock', 'papers', 'scissors)").lower()
       # quit the game
        # tie game 
       if computer_play==user_play:
            print("Game is tie!")

       elif user_play=='rock':
           if computer_play=='papers':
               # when computer_play=='papers'
              print(f"you loss!{computer_play} beats {user_play} ")
           else:
               # when computer_play=='scissors'
              print(f"you win!{user_play} beats {computer_play}")

       elif user_play=='papers':
           if computer_play=='rock':
               # when computer_play=='rock'
              print (f"you win!{user_play} beats {computer_play}")
           else:
              print (f"you loss!{user_play} beats {computer_play}")

       elif user_play=='scissors':
           if computer_play=='papers':
               print (f"you win!{user_play} beats {computer_play}")
           else:
               print (f"you loss!{computer_play} beats {user_play}")
       
       else:
           print(" Not a valid move, please try again!")
           break

               
if __name__ == '__main__':
    print("To quit the game enter any move except the valid move/n")
    winner=Play()