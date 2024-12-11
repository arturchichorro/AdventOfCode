from collections import Counter

data = """965842 9159 3372473 311 0 6 86213 48"""

line = [int(c) for c in data.strip().split()]

def change_stone_counts(counts):
    new_counts = Counter()
    for digit, freq in counts.items():
        if digit == 0:
            new_counts[1] += freq
        elif len(str(digit)) % 2 == 0: 
            d_str = str(digit)
            mid = len(d_str) // 2
            part1, part2 = int(d_str[:mid]), int(d_str[mid:])
            new_counts[part1] += freq
            new_counts[part2] += freq
        else:
            transformed = digit * 2024
            new_counts[transformed] += freq
    return new_counts

counts = Counter(line)

for _ in range(75):
    counts = change_stone_counts(counts)

result = sum(counts.values())
print(result)
