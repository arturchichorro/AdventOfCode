from typing import Dict, List, Set

with open("input.txt", "r") as file:
    data = file.read()

with open("example.txt", "r") as file:
    t_data = file.read()
Point = Dict[str, int]

DIRECTIONS: Dict[str, Point] = {
    "^": {"x": 0, "y": -1},
    ">": {"x": 1, "y": 0},
    "v": {"x": 0, "y": 1},
    "<": {"x": -1, "y": 0},
}


def allSumOfGPSCoordinates() -> int:

    parts = [lines.split("\n") for lines in data.strip().split("\n\n")]
    grid = [list(line) for line in parts[0]]
    instructions = "".join(parts[1])
    width, height = len(grid[0]), len(grid)

    walls: Set[str] = set()
    boxes: List[Point] = []
    robot = {"x": 0, "y": 0}

    for y in range(height):
        for x in range(width):
            if grid[y][x] == "@":
                robot = {"x": x * 2, "y": y}
            if grid[y][x] == "#":
                walls.add(f"{x * 2},{y}")
                walls.add(f"{x * 2 + 1},{y}")
            if grid[y][x] == "O":
                boxes.append({"x": x * 2, "y": y})

    def move_box(
        collided_box: Point, direction: Point, movements: List[Dict[str, Point]]
    ) -> bool:
        next_positions = [
            {
                "x": collided_box["x"] + direction["x"],
                "y": collided_box["y"] + direction["y"],
            },
            {
                "x": collided_box["x"] + 1 + direction["x"],
                "y": collided_box["y"] + direction["y"],
            },
        ]

        for next_pos in next_positions:
            if f"{next_pos['x']},{next_pos['y']}" in walls:
                return False

        collided_boxes = [
            box
            for box in boxes
            if any(
                (box["x"] == collided_box["x"] and box["y"] == collided_box["y"])
                is False
                and (
                    (box["x"] == next_pos["x"] or box["x"] + 1 == next_pos["x"])
                    and box["y"] == next_pos["y"]
                )
                for next_pos in next_positions
            )
        ]

        if not collided_boxes:
            return True

        conflicts = False
        for box in collided_boxes:
            if move_box(box, direction, movements):
                if not any(
                    b["x"] == box["x"] and b["y"] == box["y"]
                    for b in [m["box"] for m in movements]
                ):
                    movements.append({"box": box, "direction": direction})
            else:
                conflicts = True
                break

        return not conflicts

    for instruction in instructions:
        direction = DIRECTIONS[instruction]
        position = {"x": robot["x"] + direction["x"], "y": robot["y"] + direction["y"]}

        if f"{position['x']},{position['y']}" not in walls:
            collided_box = next(
                (
                    box
                    for box in boxes
                    if (box["x"] == position["x"] or box["x"] + 1 == position["x"])
                    and box["y"] == position["y"]
                ),
                None,
            )

            if collided_box is not None:
                movements: List[Dict[str, Point]] = []
                if move_box(collided_box, direction, movements):
                    for movement in movements:
                        movement["box"]["x"] += movement["direction"]["x"]
                        movement["box"]["y"] += movement["direction"]["y"]
                    collided_box["x"] += direction["x"]
                    collided_box["y"] += direction["y"]
                    robot = position
            else:
                robot = position

    score = sum(box["y"] * 100 + box["x"] for box in boxes)
    print(score)
    return score

allSumOfGPSCoordinates()