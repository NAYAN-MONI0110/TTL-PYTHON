import random

while True:
    closest_number=random.randint(1,100)
    player_choice= int(input("choce a number 1- 10 :"))
    computer_choice= random.randint(1,100)
    difference1= abs(player_choice-closest_number)
    difference2=abs(computer_choice-closest_number)

    if difference1<difference2:
        print("you win ","you choose :",player_choice,"closest number was :", closest_number)
        print("computer choose", computer_choice)
    elif difference1>difference2:
        print("computer win "," computer choose :", computer_choice,"clostest number was :" ,closest_number)
        print("you choose", player_choice)
    else:
         print (" the match is tie ")


    say_again=input("do you want to play again ? (yes/no) :")
    if say_again=="yes":
      continue
    else:
      break
