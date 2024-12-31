with open("input.txt", "r") as file:
    data = file.read()

lines = data.strip().split("\n")
left_arr = []
right_arr = []


for line in lines:
    left, right = map(int, line.split())
    left_arr.append(left)
    right_arr.append(right)

left_arr.sort()
right_arr.sort()

print(sum(abs(a-b) for a, b in zip(left_arr, right_arr)))