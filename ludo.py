import random


board = ["-" for _ in range(52)]
players = ["Player 1", "Player 2", "Player 3", "Player 4"]
player_positions = {player: [0, 0] for player in players}

def display_board():
    print("Ludo Board:")
    for i in range(1, 53):
        if i % 13 == 0:
            print()
        print(f"{i}:{board[i]}", end="\t")
    print()

def roll_dice():
    return random.randint(1, 6)

def move_player(player):
    print(f"{player}'s turn:")
    input("Press Enter to roll the dice...")
    dice_roll = roll_dice()
    print(f"{player} rolled a {dice_roll}")
    
    current_position = player_positions[player]
    new_position = current_position[0] + dice_roll
    
    if new_position > 52:
        new_position = new_position % 52
        
    if board[new_position] != "-":
        print(f"{player} landed on another player's piece!")
        return
    
    board[current_position[0]] = "-"
    player_positions[player] = [new_position, current_position[1] + 1]
    board[new_position] = player

def is_winner(player):
    return player_positions[player][1] == 4

def play_ludo():
    while True:
        for player in players:
            display_board()
            move_player(player)
            if is_winner(player):
                print(f"{player} wins!")
                return

if __name__ == "__main__":
    print("Welcome to Ludo!")
    play_ludo()
