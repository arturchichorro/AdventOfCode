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

secrets = parse_input(data)
for _ in range(2000):
    secrets[:] = map(get_next_secret, secrets)

print(sum(secrets))