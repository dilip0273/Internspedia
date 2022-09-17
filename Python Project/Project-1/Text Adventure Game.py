name = input("Enter Your Name: ")
print("Greeting", name, "! Welcome to text adventure Game!")
start = input("Would you play game or die?")

if start == "play":
    print("Great! Let's play the game!")
    adv = input("Want to go to the jungle or the desert?..")
    if adv == "jungle":
        print("Welcome to the mighty Amazon rainforest! Your tour guide told to wait...")
        response = input("but he has been gone a while now... follow him or wait here?")
        if response == "follow":
            print("You follow him into the trees...")
            transport = input("You see a canoe nearby. Walk or take the canoe down the river?")     
        elif response == "wait":
            print("You should wait another ten minutes, and he still isn\'t here!")
            response = input("Keep waiting or follow him?")
            if response == "follow":
                print("You head off in the direction the guide left.")
            elif response == "wait":
                print("He is finally comes back! He said the jungle is lame and the tour is over! Ending 1/6")
        else:
            print("Invalid response!, You loose!")
            quit()
        follow = input("You saw him head toward the river, there is a canoe nearby. Follow by walk or canoe?")
        if follow == "walk":
            print("As soon as you walk into the woods a huge snake crushes you to death! Ending 2/6 Found!")
        elif follow == "canoe":
            print("As soon as you get into the canoe, a huge wave washes your overhead and leaches drain your blood! \n"
                  'Ending 3/6 Found!')
            quit()
        else:
            print("Invalid response!, You loose!")
            quit()
    elif adv == "desert":
        print("Welcome to the mighty Amazon rainforest! Your tour guide told to wait...")
        response = input("but he has been gone a while now... follow him or wait here?")
        if response == "follow":
            print("You head off in the direction the guide left.")
        elif response == "wait":
            print("You should wait another ten minutes, and he still isn\'t here!")
            response = input("Keep waiting or follow him?")
            if response == "follow":
                print("You head off in the direction the guide left.")
            elif response == "wait":
                print("He is finally comes back! He said the desert is too hot and the tour is over! Ending 4/6 Found!")
        else:
            print("Invalid response!, You loose!")
            quit()
        follow = input("You saw him head toward the pyramid, there is a camel nearby. Follow by walk or camel?")
        if follow == "walk":
            print("As soon as you walk a scorpion stings you and the poison kills you! Ending 5/6 Found!")
        elif follow == "camel":
            print("The camel you are riding leads you straight to treasure and now you're a billionaire! \n"
                  "Ending 6/6 Found!")
            quit()
        else:
            print("Invalid response!, You loose!")
            quit()
    else:
        print("Invalid response!, You loose!")
        quit()
        
else:
    print("Oh! you are dead, good work...")
    quit()
    
