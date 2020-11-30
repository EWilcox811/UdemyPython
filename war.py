import random

# SUITS
# There will be 13 cards of each suit within a deck
suits = ('Hearts','Diamonds','Clubs','Spades')

# RANKS
# There will be 4 of each rank within a deck, 1 in every suit.
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
# GLOBAL DICTIONARY that will be used to give each card a value based on its rank.
# These values are what are compared to decided who wins each round.
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Card class
# each card will have a suit, rank and a simple integer value used for comparison
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"

#DECK class
class Deck:
    '''
    This will create all 52 card objects held as a list.
    Shuffle the deck through a method call. Random library shuffle() method.
    Deal out the cards to the players. Pop cards from the list.
    '''
    def __init__(self):
        # no user input because every new deck should be the same
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    # This will deal one card of the top of the deck
    def deal_one(self):
        return self.all_cards.pop()

# PLAYER class
class Player:
    '''
    Used to hold a player's list of current cards.
    A player should be able to add or remove cards from their "hand"
    We will want the player to add a single or multiple cards to their "hand"
    '''
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self, new_cards):
        #list of multiple cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        #single card
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
# GAME SETUP
player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle_deck()
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
game_on = True
round_number = 0
while game_on:
    round_number+=1
    print(f"Currently round number {round_number}")
    if len(player_one.all_cards)==0:
        print('Player one is out of cards! Player two wins!')
        game_on = False
        break
    if len(player_two.all_cards)==0:
        print('Player two is out of cards! Player one wins!')
        game_on = False
        break
    # Start a new round
    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        else:
            print("WAR!")
            if len(player_one.all_cards)<5:
                print("Player one unable to fight war.")
                print("Player two wins!")
                game_on = False
                break
            elif len(player_two.all_cards)<5:
                print("Player two unable to fight war.")
                print("Player one wins!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
