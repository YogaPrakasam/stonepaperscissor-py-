import random
print("Rock Paper Scissor")
while True:
    print(" 1.Rock  \n 2.Paper  \n 3.Scissor  \n 4.Exit  ")
    choice=int(input("Enter your Choice:"))
    if(choice==1):
        choice='Rock'

    elif(choice==2):
        choice='Paper'

    elif(choice==3):
        choice='Scissor'

    elif(choice==4):
        choice='Existing from the game'
        break

    print("Your choice: " +choice)
    computer_generated=random.randint(1,3)

    if(computer_generated==1):
        computer_generated='Rock'
    elif(computer_generated==2):
        computer_generated='Paper'
    elif(computer_generated==3):
        computer_generated='Scissor'

    print("Random choice: " + computer_generated)

    if(choice==computer_generated):
        print("Match Draw")
        print('______________________________')


    elif(choice=="Rock" and computer_generated=="Scissor"):
        print("Rock Wins")
        print("😊You wins!!!😊")
        print('______________________________')

    elif(choice=="Rock" and computer_generated=="Paper"):
        print("Paper Wins")
        print("😊Computer wins!!!😊")
        print('______________________________')



    elif(choice=="Paper" and computer_generated=="Rock"):
        print("Paper Wins")
        print("😊You wins!!!😊")
        print('______________________________')

    elif(choice=="Scissor" and computer_generated=="Paper"):
        print("Scissor Wins")
        print("😊You wins!!!😊")
        print('______________________________')   

    elif(choice=="Paper" and computer_generated=="Scissor"):
        print("Scissor Wins")
        print("😊Computer wins!!!😊")
        print('______________________________')

    elif(choice=="Scissor" and computer_generated=="Rock"):
        print("Rock Wins")
        print("😊Computer wins!!!😊")
        print('______________________________')
