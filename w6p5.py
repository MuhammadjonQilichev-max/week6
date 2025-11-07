def sort_leaderboard(leaderboard):
    # Step 1: Transform (name, score) → (-score, name)
    temp = [(-score, name) for name, score in leaderboard]
    
    # Step 2: Sort normally (ascending)
    temp.sort()
    
    # Step 3: Convert back to (name, score)
    sorted_board = [(name, -neg_score) for neg_score, name in temp]
    
    return sorted_board

leaderboard = [
    ('Alice', 88),
    ('Bob', 92),
    ('Charlie', 92),
    ('David', 85)
]
print(sort_leaderboard(leaderboard))
# Expected Output:
# [('Bob', 92), ('Charlie', 92), ('Alice', 88), ('David', 85)]


scores = [
    ('Zelda', 100),
    ('Mario', 120),
    ('Link', 100),
    ('Sonic', 100)
]
print(sort_leaderboard(scores))
# Expected Output:
# [('Mario', 120), ('Link', 100), ('Sonic', 100), ('Zelda', 100)]
