def static_func(pos=None):
    return 1

def minimax(pos, depth, alpha, beta, is_max_player):
    if depth == 0 or pos is None:
        return static_func(pos)

    if is_max_player:
        max_eval = -10000

        for child in pos:
            eval = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(alpha, eval)
            if beta <= alpha:
                break

        return max_eval

    else:
        min_eval = 10000

        for child in pos:
            eval = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return min_eval

# initial call
cur_pos = {}
minimax(cur_pos, 3, -1000, 1000, True)