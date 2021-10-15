import random

papper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
rocks =  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("input : (0) for papper,(1) for rocks and (2) for scissors "))

computer_input = random.randint(0,2)


if user_input >=3 :
    print(" you are input invalid number sir!")
else :


    stuff = [papper, rocks, scissors]

    user_answer = stuff[user_input]
    com_answer = stuff[computer_input]



    print(f"you choose {user_answer}")

    print(f"computer choose{com_answer}")

    if user_input == 0 and computer_input == 2:
        print("you lose")
    elif user_input == 2 and computer_input ==0 :
        print("you win")
    elif user_input == 1 and computer_input == 0 :
        print("you lose")
    elif user_input == computer_input :
        print("result is draw !!!")
    elif user_input < computer_input :
        print("you win!!!")
    elif computer_input < user_input :
        print("you lose")


