import sys
import random

class hangman:
    def __init__(self, difficulty='low', players=1, life=3, debug=False):
        self.difficulty = difficulty
        self.players = players
        self.life = life
        self.debug = debug

        
    
    def wordChooser(self, difficulty = 'low'):
        '''
        This chooses the word for the game.
        Args:
            difficulty: low, mid, high (str) determines the length of the word.
            (low: 3-5; mid: 6-8; high: 9-12)

        Returns:
            word

        TODO: Choose word from the internet, not from list
        '''
        if difficulty not in ['low', 'mid', 'high']:
            sys.exit("Error! The choosen difficulty is invalid. Please choose from the following difficulties: [low, mid, high].")

        words = ['ice', 'fire', 'world', 'beer', 'cloud', 'kingdom', 'civilisation', 'archipeligo', 'bus', 'driver', 'architecure', 'country', 'wire', 'sanctuary', 'sanitary', 'medium']  

        if difficulty == 'low':
            low_words = [x for x in words if 3 <= len(x) <= 5]
            word = random.choice(low_words)
            if self.debug:
                print(f"The list of available words on this difficulty {low_words}")
                print(f"The choosen word for the game on this difficulty {word}")
            return word
        elif difficulty == 'mid':
            mid_words = [x for x in words if 6 <= len(x) <= 8]
            word = random.choice(mid_words)
            if self.debug:
                print(f"The list of available words on this difficulty {mid_words}")
                print(f"The choosen word for the game on this difficulty {word}")
            return word
        else:
            high_words = [x for x in words if 9 <= len(x) <= 12]
            word = random.choice(high_words)
            if self.debug:
                print(f"The list of available words on this difficulty: {high_words}")
                print(f"The choosen word for the game on this difficulty: {word}")
            return word
        
    def hangmanGame(self):

        word = self.wordChooser(self.difficulty)
        players =  []
        lifes = []
        print('-'*38)
        print("|    Welcome to the hangman game!    |")
        print('-'*38)
        if self.players == 1:
            players.append(str(input(f"Player 1's name: ")))
        else:
            for i in range(self.players):
                players.append(str(input(f"Player {i+1}'s name: ")))
                lifes.append(self.life)
        
        if self.debug:
            print(players, lifes)

        i = self.life
        guessed_letters = [x for x in '_'*len(word)]

        print('The word:')
        print(' '.join(guessed_letters))

        while i != 0:

            for player in players:
                print(f"{player} choose a letter!")
                choosen_letter = input()
                if choosen_letter in word:
                    print("Correct!")
                    letter_index = word.index(choosen_letter)
                    guessed_letters[letter_index] = choosen_letter

                else:
                    print(f"Wrong! -1 life for {player}")
                    player_id = players.index(player)
                    lifes[player_id] = lifes[player_id]-1
                    i -= 1
                
                print('The remaining letters in the word:')
                print(' '.join(guessed_letters))

                print('-'*25)
                print('|    Remaining lives    |')
                print('-'*25)
                print(players, lifes)
        
        loser_id = lifes.index(0)
        print(f"{players[loser_id]} lost")


'''
TODO:
    Find double letters
    If found all letters last correct player wins
    If player types the word as input, the player wins
'''

        
        

if __name__ == '__main__':
    game = hangman(
        difficulty='mid',
        players=2,
        life=3,
        debug=False
    )
    game.hangmanGame()

    new_game = input('Play again? (y/n)')
    if new_game == 'y':
        game.hangmanGame()
    else:
        print("Goodbye!")

