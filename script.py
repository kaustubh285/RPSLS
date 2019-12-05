import random

def details():
    user = input("Enter user's name: ")
    computer_names=['Art Vandelay','Rusty Shackleford','Pepe Sylvia']
    Computer = random.choice(computer_names)
    print("ROCK-PAPER-SCISSORS-LIZARD-SPOCK !!!")
    print(user+" vs "+Computer)
    return user, Computer


game=True
uscore=0
cscore=0
counter=1

user , Computer = details()

while(game):

    options=['rock','paper','scissors','lizard','spock']
    coption=random.choice(options)
    
    
    while(counter <6):
        print("------------------------------------------------------------------------------")
        print("Round "+str(counter))
        uoption1=input("Enter from the following- rock, paper, scissors,lizard,spock:")
        uoption=uoption1.lower()
        print(user+" selected "+uoption)
        print(Computer+" selected "+coption)
        
        '''If user used rock'''
        
        if uoption == 'rock':
            if coption =='rock':
                print("ROCK-ROCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                break
            elif (coption =='scissors'):
                uscore=uscore+1
                print("SCISSORS-ROCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='lizard':
                cscore=cscore+1
                print("LIZARD-ROCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='spock':
                uscore=uscore+1
                print("SPOCK-ROCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            else:
                cscore=cscore+1
                print("PAPER-ROCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
        elif uoption=='scissors':
            if coption =='rock':
                cscore=cscore+1
                print("ROCK-SCISSORS......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='scissors':
                print("SCISSORS-SCISSORS......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                break
            elif coption =='lizard':
                uscore=uscore+1
                print("LIZARD-SCISSORS......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='spock':
                cscore=cscore+1
                print("SPOCK-SCISSORS......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            else:
                uscore=uscore+1
                print("PAPER-SCISSORS......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
        elif uoption == 'paper':
            if coption =='rock':
                uscore=uscore+1
                print("ROCK-PAPER......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='scissors':
                cscore=cscore+1
                print("SCISSORS-PAPER......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='lizard':
                cscore=cscore+1
                print("LIZARD-PAPER......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='spock':
                uscore=uscore+1
                print("SPOCK-PAPER......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            else:
                print("PAPER-PAPER......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                break
        elif uoption == 'lizard':
            if coption =='rock':
                cscore=cscore+1
                print("ROCK-LIZARD......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='scissors':
                cscore=cscore+1
                print("SCISSORS-LIZARD......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='lizard':
                print("LIZARD-LIZARD......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                break
            elif coption =='spock':
                uscore=uscore+1
                print("SPOCK-LIZARD......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            else:
                uscore=uscore+1
                print("PAPER-LIZARD......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break            
        elif uoption == 'spock':
            if coption =='rock':
                uscore=uscore+1
                print("ROCK-SPOCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='scissors':
                uscore=uscore+1
                print("SCISSORS-SPOCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='lizard':
                cscore=cscore+1
                print("LIZARD-SPOCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
            elif coption =='spock':
                print("SPOCK-SPOCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                break
            else:
                cscore=cscore+1
                print("PAPER-SPOCK......score("+Computer+": "+str(cscore)+" - "+ user +": "+str(uscore)+")")
                counter =counter+1
                break
        elif uoption == "exit":
            print("User chickened out")
            print("(comp "+str(cscore)+" - user "+str(uscore)+")")
            exit()
        else:
          print("###########################")
          print("Please enter correct Value!")
        
    if counter == 6:
        if uscore > cscore:
            print("User wins!")
        elif cscore > uscore:
            print("Computer wins")
        else:
            print("Tie!")
        want_to_play=input("Play again? Press y or n :")
        if want_to_play == 'y':
            game = True
            uscore=0
            cscore=0
            counter=1
        else:
            print("Thank you for playing!!")
            game = False