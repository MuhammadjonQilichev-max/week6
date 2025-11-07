def get_top_n_frequent(items, n):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    item_with_counts = []
    for item in unique_items:
        freq = items.count(item)
        item_with_counts.append((item, freq))
    print(item_with_counts)
    item_with_counts.sort()
    print(item_with_counts)
    part = item_with_counts[-n:]
    print(part)
    part.reverse()
    print(part)
    result = []
    for t in part:
        result.append(t[1])
    return result



votes = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple', 'grape']
n = 2
result = get_top_n_frequent(votes, n)
print(result)

words = ['code', 'sleep', 'eat', 'code', 'repeat', 'eat', 'code', 'sleep']
n = 3
result = get_top_n_frequent(words, n)
print(result)
