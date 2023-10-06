import random
import time

game_gesture_list=["rock","paper","scissors"]

def game_introduction():
    global name
    name=input("Enter your name before we begin the game: ")
    print("Welcome {} to my rock, paper and scissors game and this game would have two rounds".format(name))
game_introduction()

def game_instruction():
    return """            welcome to rock paper scissors !
            In this game, you wil be playing against a virtual player .Each player will choose one of the 
            following gestures:
            rock,paper or scissors.
            the rules are simple:
            rock beats scissors, scissors beats paper, paper beats rock and 
            if both players choose the same gesture then it is a TIE
            you'll play multiple rounds and we will keep track of your scores.
            The first player to reach a certain score wins the game 
            Now let's get started and have some fun ...! """

def pc_gestures():
    random.shuffle(game_gesture_list)
    computer_gesture=game_gesture_list[0]
    print("virtual player:: {}".format(computer_gesture))
    return computer_gesture

def user_gestures():
    client_gestures=input("choose between rock, paper or scissors: ")
    if client_gestures=="rock":
        print("{} :: rock".format(name))
        return "rock"
    elif client_gestures=="paper":
        print("{} :: paper".format(name))
        return "paper"
    elif client_gestures=="scissors":
        print("{} :: scissors".format(name))
        return "scissors"
    else:
        print(" you can only choose between rock, paper or scissors")

def main_game():
    game_instruction_question=input("if you are new to the rock, paper and scissors game you can read the game instruction?\n Enter either yes or no to read the game instruction: ")
    if game_instruction_question.lower()=="yes":
        print(game_instruction())
        print("The game will start after 9 secs just to give you the time to read the instructions")
        time.sleep(9)
    else:
        pass
    print("let the game begin!!")
    time.sleep(1)
    print("rock paper scissors!")
    time.sleep(1)
    print("rock paper scissors!!")
    time.sleep(1)
    print("rock paper scissors!!!")
    time.sleep(1)
    #storing the functions user_gestures and pc_gestures into variables
    player_gesture=user_gestures()
    virtual_gesture=pc_gestures()
    player_score=0#initializing player score
    virtual_player_score=0#initializing virtual player score
    player_score2=0#initializing for the second round
    virtual_player_score2=0#initializing for the second round

    print(" Since the virtual player chose {} and you chose {} ".format(virtual_gesture,player_gesture))

    if player_gesture == virtual_gesture:
        print("The game is a TIEE!")
        print("since its a tie ,no points/score awarded!")
    elif player_gesture=="rock":
        if virtual_gesture=="scissors":
            print("Dear {} you won the game!! ".format(name))
            player_score+=1
        elif virtual_gesture=="paper":
            print(" The virtual player WON!!")
            virtual_player_score+=1
    elif player_gesture=="scissors":
        if virtual_gesture=="paper":
            print("Dear {} you won the game!! ".format(name))
            player_score+=1
        elif virtual_gesture=="rock":
            print(" The virtual player WON!!")
            virtual_player_score+=1
    elif player_gesture=="paper":
        if virtual_gesture=="rock":
            print("Dear {} you won the game!! ".format(name))
            player_score+=1
        elif virtual_gesture=="scissors":
            print(" The virtual player WON!!")
            virtual_player_score+=1
    print("For the first round, the virtual player score is {}points and the player score is {}points".format(virtual_player_score,player_score))
    print("Having concluded the first round would you like to go for another round?")
    user_game_rounds=input("Enter either yes or no for the second round: ")
    if user_game_rounds.lower()=="yes":
            print("let the game start.!")
            time.sleep(1)
            print("rock paper scissors!")
            time.sleep(1)
            print("rock paper scissors!!")
            time.sleep(1)
            print("rock paper scissors!!!")
            time.sleep(1)
        #storing the functions user_gestures and pc_gestures into variables
            player_gesture=user_gestures()
            virtual_gesture=pc_gestures()
            print(" Since the virtual player chose {} and you chose {} ".format(virtual_gesture,player_gesture))

            if player_gesture == virtual_gesture:
                print("The game is a TIEE!")
                print("since its a tie again, no points/score awarded")
            elif player_gesture=="rock":
                if virtual_gesture=="scissors":
                    print("Dear {} you won the game!! ".format(name))
                    player_score2+=1
                elif virtual_gesture=="paper":
                    print(" The virtual player WON!!")
                    virtual_player_score2+=1
            elif player_gesture=="scissors":
                if virtual_gesture=="paper":
                    print("Dear {} you won the game!! ".format(name))
                    player_score2+=1
                elif virtual_gesture=="rock":
                    print(" The virtual player WON!!")
                    virtual_player_score2+=1
            elif player_gesture=="paper":
                if virtual_gesture=="rock":
                    print("Dear {} you won the game!! ".format(name))
                    player_score2+=1
                elif virtual_gesture=="scissors":
                    print(" The virtual player WON!!")
                    virtual_player_score2+=1              
    elif user_game_rounds.lower()=="no":
        print(" Thanks for playing my rock paper and scissors game .Hope you enjoyed the game?")
    else:
        print("input either yes or no!!")
    print("For the second round, the virtual player score is {}points and the player score is {}points".format(virtual_player_score2,player_score2)) 
    total_virtual_points=virtual_player_score+virtual_player_score2
    total_player_points=player_score+player_score2
    print(" Therefore, for the two rounds the virtual player point is {} points and player point is {} points".format(total_virtual_points,total_player_points))

main_game()




