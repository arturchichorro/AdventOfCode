from collections import Counter

with open("input.txt", "r") as file:
    data = file.read()

lines = data.strip().split("\n")

left_arr = []
right_arr = []

for line in lines:
    left, right = map(int, line.split())
    left_arr.append(left)
    right_arr.append(right)

counts = Counter(right_arr)

res = sum(left * counts[left] for left in left_arr)

print(res)