with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
    
def mix(number, value):
    return number ^ value

def prune(number):
    return number % 16777216

def get_next_secret(number):
    number = prune(mix(number * 64, number))
    number = prune(mix(number // 32, number))
    number = prune(mix(number * 2048, number))
    return number

def parse_input(input):
    return list(map(int, input.strip().split("\n")))

def most_bananas(input):
    
    secrets = parse_input(input)
    ranges = {}
    
    for secret in secrets:
        
        copy = secret
        visited = set()
        changes = []

        for _ in range(2000):
            next_secret = get_next_secret(copy)
            changes.append((next_secret % 10) - (copy % 10))
            copy = next_secret

            if len(changes) == 4:
                key = ",".join(map(str, changes))
                if key not in visited:
                    if key not in ranges:
                        ranges[key] = []
                    ranges[key].append(next_secret % 10)
                    visited.add(key)
                changes.pop(0)
    
    return max(sum(vals) for vals in ranges.values())
        
print(most_bananas(data))