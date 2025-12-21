board = [[" "]*3 for _ in range(3)]

def print_board():
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("-"*9)

def win(p):
    return any(
        all(board[r][c] == p for c in range(3)) or
        all(board[c][r] == p for c in range(3))
        for r in range(3)
    ) or all(board[i][i] == p for i in range(3)) or \
       all(board[i][2-i] == p for i in range(3))

def draw():
    return all(cell != " " for row in board for cell in row)

player = "X"

while True:
    print_board()
    try:
        move = input(f"\nPlayer {player} (row col) or q: ")
        if move.lower() == "q":
            break
        r, c = map(int, move.split())
        if not (1 <= r <= 3 and 1 <= c <= 3):
            print("Out of range!")
            continue
        r -= 1; c -= 1
        if board[r][c] != " ":
            print("Cell occupied!")
            continue
        board[r][c] = player
        if win(player):
            print_board()
            print(f"\nPlayer {player} wins!")
            break
        if draw():
            print_board()
            print("\nDraw!")
            break
        player = "O" if player == "X" else "X"
    except:
        print("Invalid input!")
