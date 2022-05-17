from random import choice
class Game:
    def __init__(self):
        self.deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        self.user_hand = []
        self.computer_hand = []
        self.user_total = 0
        self.computer_total = 0
    
    def deal(self):
        self.user_hand = [choice(self.deck), choice(self.deck)]
        self.computer_hand = [choice(self.deck), choice(self.deck)]
        self.user_total = sum(self.user_hand)
        self.computer_total = sum(self.computer_hand)
        print(f"""Your cards: {self.user_hand}, current score: {self.user_total}
            Computer's first card: {self.computer_hand[0]}""")


    def add_card(self, hand):
        new_card = choice(self.deck)
        if hand == self.user_hand:
            self.user_hand.append(new_card)
            self.user_total += new_card
        elif hand == self.computer_hand:
            self.computer_hand.append(new_card)
            self.computer_total += new_card
    
    def user_plays(self):
        while True:
             user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
             if user_choice == 'y':
                 self.add_card(self.user_hand)
                 if self.user_total <= 21:
                    print(f"""Your cards: {self.user_hand}, current score: {self.user_total}
                    Computer's first card: {self.computer_hand[0]}""")
                 else:
                     break
             else:
                break
    
    def computer_plays(self):
        while self.computer_total < 17:
            self.add_card(self.computer_hand)

    def compare(self):
        print(f"Your final hand: {self.user_hand}, final score: {self.user_total}")
        print(f"Computer's final hand: {self.computer_hand}, final score: {self.computer_total}")
        if self.user_total == 21:
            print("You have blackjack, you win!")
        elif self.user_total > 21:
            print("You went over, you lose")
        elif self.computer_total > 21:
            print("Computer went over, you win!")
        elif self.user_total > self.computer_total:
            print("You have the higher hand, you win!")
        else:
            print("You have the lower hand, you lose!")
         
    def play(self):
        self.deal()
        self.user_plays()
        self.computer_plays()
        self.compare()
        
        