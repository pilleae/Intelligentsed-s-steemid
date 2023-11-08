import random

def print_piles(piles):
    print("Current Piles:")
    for i, pile in enumerate(piles):
        print(f"Pile {i + 1}: {pile} objects")
    print()

def get_valid_moves(piles):
    moves = []
    for i, pile in enumerate(piles):
        for j in range(1, min(pile, 3) + 1):
            moves.append((i, j))
    return moves

def apply_move(piles, move):
    pile_index, num_objects = move
    piles[pile_index] -= num_objects

def nim_sum(piles):
    nim_sum_value = 0
    for pile in piles:
        nim_sum_value ^= pile
    return nim_sum_value

def is_game_over(piles):
    return all(pile == 0 for pile in piles)

def player_move(piles):
    print_piles(piles)
    valid_moves = get_valid_moves(piles)
    while True:
        try:
            pile_index = int(input("Enter pile number (1, 2, or 3): ")) - 1
            num_objects = int(input("Enter number of objects to remove: "))
            if (pile_index, num_objects) in valid_moves:
                return (pile_index, num_objects)
            else:
                print("Invalid move")
        except (ValueError, IndexError):
            print("Invalid input")

def computer_move(piles):
    _, move = minimax(piles, 5, True) 
    pile_index, num_objects = move
    max_objects = min(num_objects, 3)
    return pile_index, max_objects

def evaluate(piles):
    nim_sum_value = nim_sum(piles)
    if nim_sum_value == 0:
        return 1
    else:
        return -1

def minimax(piles, depth, maximizing_player):
    if depth == 0 or is_game_over(piles):
        return evaluate(piles), None

    moves = get_valid_moves(piles)

    if maximizing_player:
        max_score = float("-inf")
        best_move = None

        for move in moves:
            new_piles = piles.copy()
            apply_move(new_piles, move)
            score, _ = minimax(new_piles, depth - 1, False)
            if score > max_score:
                max_score = score
                best_move = move

        return max_score, best_move

    else:
        min_score = float("inf")
        best_move = None

        for move in moves:
            new_piles = piles.copy()
            apply_move(new_piles, move)
            score, _ = minimax(new_piles, depth - 1, True)
            if score < min_score:
                min_score = score
                best_move = move

        return min_score, best_move

def play_nim():
    piles = [random.randint(1, 10) for _ in range(3)]
    current_player = 0

    print("Each turn, remove any number of objects from a single pile.")
    print("The player who removes the last object loses.")

    while not is_game_over(piles):
        if current_player == 0:
            move = player_move(piles)
        else:
            move = computer_move(piles)
            print(f"Computer removes {move[1]} objects from Pile {move[0] + 1}.")
        apply_move(piles, move)
        current_player = 1 - current_player

    if current_player == 0:
        print("Congratulations! You win!")
    else:
        print("Computer wins! Better luck next time.")

if __name__ == "__main__":
    play_nim()
