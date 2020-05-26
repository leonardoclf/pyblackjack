import random


cardC = ["A of Club", "2 of Club", "3 of Club", "4 of Club", "5 of Club", "6 of Club", "7 of Club", "8 of Club", "9 of Club", "10 of Club", "J of Club", "Q of Club", "K of Club"]
cardD = ["A of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "J of Diamonds", "Q of Diamonds", "K of Diamonds"]
cardH = ["A of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "J of Hearts", "Q of Hearts", "K of Hearts"]
cardS = ["A of Spade", "2 of Spade", "3 of Spade", "4 of Spade", "5 of Spade", "6 of Spade", "7 of Spade", "8 of Spade", "9 of Spade", "10 of Spade", "J of Spade", "Q of Spade", "K of Spade"]



deck = cardC + cardD + cardH + cardS

def draw(numberCards):
    drew = random.sample(deck, numberCards)
    for card in drew:
        deck.remove(card)
    return drew

def hit(hand):
    card = draw(1)
    card = ''.join(card)
    hand.append(card)

def totalPoints(hand):
    points = 0
    for card in hand:
        try:        
            points += int(card[0:2])
        except:
            if card[0] in ["Q", "J", "K"]:
                points += 10
            elif card[0] == "A":
                for i in (range(len(hand))):
                    if hand[i][:1] == "K" or hand[i][:1] == "Q" or hand[i][:1] == "J":
                        points += 11
                        break
                    else:
                        points += 1
                        break
    return points

def start_msg():
    welcome_msg = """
|------------------------------------------|
|             BlackJack                    |
|            Version 0.02                 |
|------------------------------------------|
"""
    menu_msg = """
|------------------------------------------|
|  Press 1 - to play                       |
|  Press 2 - to quit                       |
|------------------------------------------|
"""
    print(welcome_msg)
    print(menu_msg)
    menu = input("... ")
    if menu == "2":
        exit()
    
        


start_msg()




#first action

player_hand = draw(2)
dealer_hand = draw(2)    

print(f'Your hand: {player_hand[0]} and {player_hand[1]}')
print(f'\nDealer hand: {dealer_hand[0]} and tapped card')
print('\nWhat you want to do? hit or stand')





# player turn 
print("\nPlayer Turn")
while True:
    if totalPoints(player_hand) < 21:
        player_choice = input("... ")
        if player_choice == "hit":
            hit(player_hand)
            print(player_hand)
            print(totalPoints(player_hand))
            if totalPoints(player_hand) > 21:
                print("\nPlayer busted")
                print("Game over")
                exit()
        elif player_choice == "stand":
            break
    else:
        break
    

#dealer turn 
print("\nDealer Turn")
print(f'Dealer has {dealer_hand[0]} and {dealer_hand[1]}')
while True:
    if totalPoints(dealer_hand) < 18:
        hit(dealer_hand)
        print(dealer_hand)
        if totalPoints(dealer_hand) > 21:
            print("\nDealer busted")
            print("Player win")
        elif totalPoints(dealer_hand) == 21:
            print("\nDealer win")
            exit()
    else:
        print("\nDealer win")
        exit()





    













            

        
 




