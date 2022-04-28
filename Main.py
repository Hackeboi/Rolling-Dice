import random

roll_again='y'

while roll_again=='y'
 print('Rolling the dice')
 print('The value of the dice')
 dice1=random.randint(1,6)
 dice2=random.randint(1,6)
 print(dice1,dice2)
 roll_again=input("Wanna roll the dice again(y/n): ")
