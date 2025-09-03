class GameBrain:
    def __init__(self):
        self.base_board = []
        self.welcome_msg()

### Beginning Of Game / Reset Board Setup ###
    def welcome_msg(self):
        print("\nWelcome to Tic Tac Toe, Get three in a row to win!\n")
        self.get_board()

    def update_board(self):
            with open ('board.txt') as file:
                board = file.readlines()
                for line in board:
                    print(line, end='')

    def get_board(self):
        with open ('board.txt') as file:
            board = file.readlines()
            for line in board:
                print(line, end='')
            self.base_board = board
    
    def reset_board(self, code):
        with open ('board.txt', 'r+') as file:
            board = file.readlines()
        
        for i in range(3,10):
            board[i] = self.base_board[i]
        
        with open ('board.txt', 'w') as file:
                file.writelines(board)

        if code == 1:
            self.update_board()
                
### Mid-Game / End-Game Placement and Checks ###
    def get_input(self, count):
        try:
            u_input = input(f'\nPlayer {self.check_player(count)}, Enter your location:\n')
            return u_input
        except KeyboardInterrupt:
            self.reset_score()
            self.reset_board(1)

    def place_marker(self, u_input, player):
        found = False
        if player == 1:
            marker = 'X'
        else: 
            marker = 'O'

        with open ('board.txt', 'r+') as file:
            board = file.readlines()

        for i in range(3, 10):
            if str(u_input) in board[i]:
                board[i] = board[i].replace(str(u_input), marker)
                found = True
                break
            if not found and i == 9:
                 return False, print('Position taken, Try Again!'), self.update_board()

        with open ('board.txt', 'w') as file:
                file.writelines(board)

        self.update_board()

    def detect_end(self):
        with open ('board.txt', 'r') as file:
             lines = file.readlines()

        board = []

        board_lines = (lines[i] for i in [5,7,9])
        for line in board_lines:
             row = (line[4], line[12], line[20])
             board.append(row)

        for row in board:
            if row[0] == row[1] == row[2] and row[0] in ['X', 'O']:
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ['X', 'O']:
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ['X', 'O']:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ['X', 'O']:
            return board[0][2]

        if not any(char.isdigit() for row in board for char in row):
            self.call_draw()

        return None
    
    def check_player(self, count):
        if count % 2 == 0:
            player = 2
        else:
            player = 1
        return player

### End Game and Reset ###
    def winner(self, player_num):
        with open ('board.txt', 'r') as file:
            lines = file.readlines()
            
        scoreboard = lines[-1]
        
        parts = scoreboard.split(' ')

        if player_num == 1:
            parts[2] = str(int(parts[2])+1)
        elif player_num == 2:
            parts[4] = str(int(parts[4])+1)

        scoreboard = ' '.join(parts)

        with open ('board.txt', 'w') as file:
                lines[-1] = scoreboard
                file.writelines(lines)
        print('\n=========================\n')
        print(f'\nCongratulations Player {player_num}, You won this round!\n')
        self.reset_board(1)

    def call_draw(self):
        print('\n=========================\n')
        print(f'\nDraw! No-one wins this round.\n')
        self.reset_board(1)
        return 'D'
    
    def reset_score(self):
        with open ('board.txt', 'r') as file:
            lines = file.readlines()
            
            scoreboard = lines[-1]
            
            parts = scoreboard.split(' ')

            parts[2] = str(int(parts[2])*0)
            parts[4] = str(int(parts[4])*0)

            scoreboard = ' '.join(parts)

        with open ('board.txt', 'w') as file:
            lines[-1] = scoreboard
            file.writelines(lines)
            