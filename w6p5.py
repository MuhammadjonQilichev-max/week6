def sort_leaderboard(leaderboard):
    temp = [(-score, name) for name, score in leaderboard]
    temp.sort()
    sorted_board = [(name, -neg_score) for neg_score, name in temp]
    return sorted_board

leaderboard = [
    ('Alice', 88),
    ('Bob', 92),
    ('Charlie', 92),
    ('David', 85)
]
print(sort_leaderboard(leaderboard))

scores = [
    ('Zelda', 100),
    ('Mario', 120),
    ('Link', 100),
    ('Sonic', 100)
]
print(sort_leaderboard(scores))
