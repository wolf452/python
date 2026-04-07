class players:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid name, please enter a valid name")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("Invalid symbol, please enter a valid symbol")


class menu:
    def display_main_menu(self):
        print("""Choose one of the following options:
1 - Start a new game
2 - Exit the game
""")
        choice = int(input("Enter your choice (1 or 2): "))
        return choice

    def choose_endgame_menu(self):
        menu_text = """Choose one of the following options:
1 - Reset the game
2 - Exit the game
"""
        choice = int(input(menu_text))
        return choice


class board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i + 3]))
            print("-" * 5)

    def update_board(self, choice, symbol):
        if self.is_valid(choice):
            self.board[choice - 1] = symbol
            return True
        return False

    def is_valid(self, choice):
        return self.board[choice - 1].isdigit()

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class game:
    def __init__(self):
        self.players = [players(), players()]
        self.menu = menu()
        self.board = board()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == 1:
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your name:")
            player.choose_name()
            player.choose_symbol()

    def play_game(self):
        while True:
            self.turn_player()

            if self.check_win():
                self.board.display_board()
                print(f"{self.players[self.current_player_index].name} wins 🎉")
                choice = self.menu.choose_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                break

            if self.check_draw():
                self.board.display_board()
                print("It's a draw 🤝")
                choice = self.menu.choose_endgame_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                break

    def turn_player(self):
        player = self.players[self.current_player_index]
        self.board.display_board()

        while True:
            try:
                cell_choice = int(input(f"{player.name}, choose a cell (1-9): "))
                if 1 <= cell_choice <= 9 and self.board.is_valid(cell_choice):
                    self.board.update_board(cell_choice, player.symbol)
                    break
                else:
                    print("Invalid choice, try again")
            except ValueError:
                print("Please enter a number")

        self.switch_player()

    def check_win(self):
        win_comb = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for comb in win_comb:
            if self.board.board[comb[0]] == self.board.board[comb[1]] == self.board.board[comb[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def quit_game(self):
        print("Thank you for playing 👋")


# تشغيل اللعبة
if __name__ == "__main__":
    game = game()
    game.start_game()
