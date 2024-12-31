with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()

def solve_part1(input):
    numpad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2),
    }
    dirpad = {
        '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    }

    def create(keypad, invalid_coords):
        graph = {}
        for a, (x1, y1) in keypad.items():
            for b, (x2, y2) in keypad.items():
                path = '<' * (y1 - y2) + 'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
                if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
                    path = path[::-1]
                graph[(a, b)] = path + 'A'
        return graph
    
    numpad_graph = create(numpad, (3, 0))
    dirpad_graph = create(dirpad, (0, 0))

    def convert(sequence, graph):
        conversion = ''
        prev = 'A'
        for char in sequence:
            conversion += graph[(prev, char)]
            prev = char
        return conversion
    
    total_complexity = 0
    for button_presses in input.split('\n'):
        conversion = convert(button_presses, numpad_graph)
        conversion = convert(conversion, dirpad_graph)
        conversion = convert(conversion, dirpad_graph)
        total_complexity += int(button_presses[:-1]) * len(conversion)

    return total_complexity

print(solve_part1(data))