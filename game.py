import random
def coder_decision(computers, i):
    coder_decision = input("Coder player do you want to remove bug(STOP to give up)? (y/n)")
    if coder_decision == "y":
        computers[i] = False
    elif coder_decision == "Stop":
        print("Yay the Virus won")
        return
    
def virus_decision(computers, i):
    virus_decision = input("Virus player do you want to add bug(STOP to stop)? (y/n)") 
    if virus_decision == "y":
        computers[i] = True
    elif virus_decision == "Stop":
        return

def play_game():
    bugs = random.sample(range(6), 2)
    computers = [(i in bugs) for i in range(6)]
    print("Hello this is the Computer Bug game lets begin:")
    while True:
        for i in range(len(computers)):
            print(computers)
            if computers[i] == True:
                coder_decision(computers, i)
            else:
                virus_decision(computers, i)
                
                
            if not (True in computers):
                print("The coder has won yay")
                return

play_game()
