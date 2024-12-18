t_data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

DIR = [
    { "x": 1, "y": 0 },
    { "x": 0, "y": 1 },
    { "x": -1, "y": 0 },
    { "x": 0, "y": -1 },
]

def parse_grid(input):
    maze = input.strip().split("\n")
    width, height = len(maze[0]), len(maze)

    start, end = { "x": 0, "y": 0 }, { "x": 0, "y": 0 }
    forward = {}
    reverse = {}

    for y in range(height):
        for x in range(width):
            if maze[y][x] == "S":
                start = { "x": x, "y": y }
            if maze[y][x] == "E":
                end = { "x": x, "y": y }

            if maze [y][x] != "#":
                for i, direction in enumerate(DIR):
                    position = { "x": x + direction["x"], "y": y + direction["y"] }

                    key = f"{x},{y},{i}"
                    move_key = f"{position["x"]},{position["y"]},{i}"
