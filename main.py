import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10
    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer
    
    @property
    def counter(self):
        return self._counter
    
    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self,):
        return self._die.roll()
    

class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer
    

    def play(self):
        print("+++++++++++++++++")
        print("Welcome To Dice Game")
        print("+++++++++++++++++")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break
    def play_round(self):
        self.print_round_welcome()

        player_value  = self._player.roll_die()
        computer_value = self._computer.roll_die()

        self.show_the_dies(player_value, computer_value)

        if player_value > computer_value:
            print("You won the round")
            self.update_counters(winner=self._player, looser=self._computer)
        elif computer_value > player_value:
            print("Computer Won the round")
            self.update_counters(winner=self._computer, looser=self._player)
        else:
            print("its a tie")

        self.show_counters()

        

    def print_round_welcome(self):
        print("++++++New Round++++++")
        input("press any key to roll the dice")

    def show_the_dies(self, player_value, computer_value):
        print(f"your die: {player_value}")
        print(f"Computer die: {computer_value}")

    def update_counters(self, winner, looser):
        winner.decrement_counter()
        looser.increment_counter()

    def show_counters(self):
        print(f"Your Counter: {self._player.counter}")
        print(f"computer Counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(self._computer)
            return True
        else:
            return False
        
    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n_______________")
            print("Game Over")
            print("\n_______________")
            print("Computer Won")
            print("_______________")
        else:
            print("\n_______________")
            print("Game Over")
            print("\n_______________")
            print("You Won")
            print("_______________")

        



player_die = Die()
computer_die = Die()
player = Player(player_die, is_computer=False)
com_player = Player(computer_die, is_computer=True)

game = DiceGame(player, com_player)

game.play()


        
    


        