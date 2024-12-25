import heapq
from collections import defaultdict

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

t1_data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

data = """#############################################################################################################################################
#...........#.....#...........#.......#...#.......#.#...........#.......#...#.............#.#.....#.........#...#.........#................E#
#.#########.#.#.#.#########.#.###.###.#.###.#.###.#.#.###.#####.#.###.###.#.#.###.#######.#.#.#.#.#.#####.#.#.#.#.#######.#.#.#####.###.#.#.#
#.#.......#...#.#...........#.....#...#.....#.#...#.....#.....#...........................#...#.#.#.....#.#...#...#.....#.#.#.........#...#.#
#.#.#####.#####.###################.#########.#.###.#######.#.#.#.#.#######.###.#.#.#.#########.#####.###.#########.#.#.#.###############.#.#
#.#.#.......#...#...........#.......#.........#...#.#.#...............#...#...#.#.#...........#.....................#.#.........#.......#.#.#
#.#.#.#####.#.###.#####.###.#.#########.#.#######.#.#.#.#.#.#.#######.###.###.#.#.###########.#####.#.#.###.#.#.###.#.#########.#.#####.###.#
#.#.#.#...#.#.#...#...#...#...#.........#.....#...#...#.#.#.#...............#...#...........#.......#.#.#...#.#...#.#.#...#.......#.........#
#.#.###.#.#.#.#.###.#.###.#####.#.###.###.###.#.#######.#.#####.###########.#############.#.#.#######.#.#.#.###.#.#.#.#.#.#.#######.#######.#
#.#.....#.#...#.#...#.#.#.#.......#...#.#...#...#.......#.....#.#.......#.....#.........#.#.#.#.......#.#.#.......................#...#...#.#
#########.###.###.###.#.#.#.#######.###.#.#.#######.#.#######.#.#.#####.#######.#######.###.###.#####.#.#############.#.#.###.###.###.#.#.#.#
#.......#...#.....................#.#.......#.....#.#.#.....#.#.#.#...........#...#...#.#...#...#...#.#.....#.......#.#.#.....#.#...#.#.#.#.#
#.#####.###.###.#####.#.###.#.###.#.#.###.#####.#.#.#.#.###.#.###.###########.###.#.#.#.#.###.###.#.#.#####.#.#####.#.#.#######.###.###.#.###
#.#.#...#...#...#.#...#.#.....#.#...#.#.........#.#.#.....#.#...#.......#...#...#.#.....#.....#...#.#.#.....#.#.....................#...#...#
#.#.#.###.###.###.#.###.#.#.###.#####.###.#.#####.#.#######.###.#.#####.#.#.#.#.#.#.#.#####.###.###.###.#####.#.#.###.#.#.#.#.#.#.###.#####.#
#.#...#.......#...#.#.....#.......#.#...#.#.#.....#...#.....#...#.#.....#.#.#...#.#.......#.#...#...#...#...#.#.#.......#.#...........#.....#
#.#.#########.###.#.#########.###.#.###.###.###.#####.#.#.###.###.#.#.#.#.#.#.###.#######.###.###.###.###.#.#.#.#########.#########.#.#.###.#
#.................#...#.....#.#...#...#...#...#.......#...#...#.....#.#.#.#.#.....#.....#.#...#.#...#.....#...............#.......#...#.#...#
#.#########.#.#.#.###.#.###.#.#.###.#####.###.#########.###.#.#####.#.#.#.#.#########.###.#.###.###.#.###############.###.#.#####.#.#.#.#.#.#
#.........#.#...#.#...#...#...#...#.....#...#...#.....#...#.#.......#...#.#.....#.....#...#.#.#.....#...........#...#...#.#...#.#...#.#...#.#
#.#.#####.#.#####.#.#####.#######.#.###.###.###.#.###.#.#.#.#.#.#########.#####.###.#.#.###.#.#.###############.#.#.###.#.###.#.###.#.#.#.###
#.#.#.....#.#.....#.....#.#...#...#.......#.#...#...#...#.#.#.#.......#...#.........#.#...#.#...#.........#...#...#.....#...#.#...#.#...#...#
#.#.#.#####.###.#######.#.###.#.#####.#.###.#.###.#.###.#.#.#########.#.#.###############.#.###.#####.###.#.#.#########.#####.#.###.#.#.#.#.#
#.#.#.....#...#.......#.#...#...........#...#...#.#...#...#.........#.#.#.........#.......#...#.......#.#.#.#...#.#.....#.....#.#...#.#...#.#
#.#.#.###.###.#######.#.#.#.#############.#####.#.###.###.#########.#.#.#########.#.#########.#########.#.###.#.#.#.#####.#####.#.#####.#.#.#
#.#.#.#.#...#...#.....#.#.#.#.......#...#.#.....#...#...#...#.......#.#.#.....#...#.........#.#.#.........#...#...#.#...#.#.....#.#.....#...#
#.#.#.#.#.#####.#.#####.###.#.#####.#.#.#.#.#####.#.###.###.#.#######.#.#.###.#.#.#########.#.#.#.#########.#######.#.###.#.#.###.#.#.#.#.###
#.#.#...#.....#.#...#...#...#.....#...#.#.#.#.#...#...#.#...#.#.......#...#...#.#.#.#.....#...#.#.#.#.................#...#.#.#...#.#.#.....#
###.###.###.#.#.#.###.###.#.#####.#####.#.#.#.#.#####.#.#.###.#.###########.###.#.#.#.###.#####.#.#.#.#.###############.###.###.###.#.#.#.#.#
#...#.....#...#.#.#...#...#...#...#...#...#.#...#.....#.#.#.#...#...#.......#...#...#.#.....#.....#...........#.........#.....#.....#...#...#
#.#####.#####.#.###.#####.#.###.###.#.#####.#.#####.###.#.#.###.#.###.#######.#######.#.###.#.#####.#.#######.#.#########.###.#####.###.#.#.#
#.......#...#.#.....#...#.#.....#...#...#...#.#.....#...#.#...........#.....#...#.....#.....#.#...#...#...#...#.#.#...#...#.#.........#.#.#.#
#.#####.#.#.#.#######.#.#.#.#####.#####.###.#.#.###.#.#.#.#########.#.#.###.###.#.#########.#.###.#.###.#.#####.#.#.#.#.###.#########.#.#.###
#...#.#...#.#.....#...#...#...#.......#.....#...#...#.#.........#...#...#.....#.....#...#...#...#.#.#.#.#.....#.#...#.#...............#.#...#
###.#.#.###.#.###.#.#.###.###.#.#####.###########.###.#########.#.#.###.#.###.#####.#.#.#.#####.#.#.#.#.#####.#.#####.#######.#.#.#.#####.#.#
#.#.#.#...#.....#.#.#...#...#.#.#.....#.......#...#.#.....#...#...#.......#...#...#...#.#...#...#...#.#.#.....#.....#.........#.#.#.......#.#
#.#.#.#.#.###.#.#.#.###.###.#.###.###.#.###.###.###.#####.#.#############.#.###.#.###.#.###.#.###.###.#.###.#######.#.###.#.###.#.#######.#.#
#...#...#.#.....#.....#...#.#.#...#.....#...#...#.....#...#...............#.#...#...#.#...#...#.#...#.#...#.....#...#.......................#
#.#######.#.#.###########.#.#.#.###.#.#######.###.#####.#####.###.#########.#.#####.#####.#####.###.#.###.#####.#.#####.###.#.#####.#.#.###.#
#...#.....#...#...........#.#.#.#...#.#.....#.#.......#...............#.....#.#...#.#...#.....#...#.#...#.#...#.#...#.#...#.#.#...#...#.#...#
###.#.###.###.#.#.#########.#.#.#.#####.###.#.#####.#.#####.###########.#####.#.#.#.#.#.#.#.#.###.#.#.#.#.#.###.###.#.###.#.#.#.#.###.#.#.###
#...#...#...#.#.#...#.#.....#.#.#...#...#.#.#.....#.#.#...#...#...#...#.#.......#...#.#.#.#.#.....#...#.#.#...#...#.#.......#.#.#...#.#.#.#.#
#.###.#.#####.#.###.#.#.#####.#.#.#.#.###.#.#.#.#.###.#.#.###.#.#.#.#.#.#.###.###.###.#.###.#####.#.#####.###.###.#.###.#####.#.###.###.#.#.#
#.#...#.#.....#...#.#...#.....#.#.#.#.#...#.#...#...#...#...#...#...#...#...#...#...#.#.#...#...#.#.#...#.#...#...#...#...#...#.#.#.....#...#
#.#####.#.#.#.#####.###.#.#####.###.#.#.#.#.#######.#####.#################.###.###.#.#.#.###.###.#.#.#.#.#.#.#.#####.#####.###.#.#########.#
#.#.....#.#.#.....#.......#...#...#.....#.#.......#.#...#...........#.....#.#...#.....#...#.......#.#.#...#.#.............#...#.#...#.......#
#.#.###.#.###.###.#.#######.#.#.#.###.#####.#####.#.#.#.#.#####.#.#.###.#.###.#####.#######.#######.#.#####.#######.#.###.###.#.#.###.#######
#...#...#.......#.#.#.......#.......#.#...#.#.#...#...#...#...#.#.#...#.#.....#.....#...#...#.......#...#.#.......#.#...#.....#.#...#...#...#
###.#########.###.#.###.#.#########.#.#.#.#.#.#.#########.#.#.#.#.###.#.###.#.#.###.#.#.#.#.#.#########.#.#.###.###.###.#######.#.#.###.###.#
#...#...#.....#...#.....#...#...#...#.#.#...#...#.#.....#...#.#.#.#...#.#.#.#.#...#.#.#.....#.#.....#...#.#.#.#.....#.#.#.......#.#...#.#...#
#.###.#.#.###.#.###.#######.#.#.#.###.#.#####.###.#.#.#######.###.#.###.#.#.#.###.#.#.#####.#.#.###.#.###.#.#.#######.#.#.#######.#.###.#.#.#
#...#.#...#.....#...#.........#...#...#.#...#.#...........#.#...#.......#...#...#.#.#.#...#.#.#.#...#.#.....#...#...#...#.#.......#...#...#.#
###.#.#.#########.#.#.#.#########.#.###.###.#.#####.###.#.#.###.#.#######.###.###.#.###.#.###.#.#.###.###.###.#.###.#.#.#.#.#########.#####.#
#...#.#.#...#.....#.#.#.........#.#.#.#...#.#.....#.#...#.....#...#...#...#.#.....#.....#.....#.....#...#.#...#.....#.#...#.....#.....#.....#
#.###.###.#.#.#####.#.#####.###.#.#.#.###.#.#####.###.#.#####.#####.#.#.###.#.#################.###.###.#.#.#.###.###.#.###.#.###.###.#.#####
#.........#.#.#.#...#.#.#...#.#.#.....#.#.#.....#...#.#.#...#.#.....#.#.#...............#.......#.#.....#.#.....#.#...#...#...#...#...#.....#
###.#.#.###.#.#.#.###.#.#.###.#.#####.#.#.#.###.###.#.###.#.###.###.###.#.###############.#######.#######.###.#.###.#####.###.#.###.#.#####.#
#...#...#...#.#.....#...#...#.#.....#...#.#.#...#...#...#.#...#.#.#.#...#.#...#...........#.............#...#.#.....#.#...#...#.....#.....#.#
#########.###.#######.#####.#.#####.#####.#.#.#.#.#####.#.###.#.#.#.#.###.#.#.#.###.#########.#############.#.#######.#.###.#########.###.#.#
#.......#.#.#.......#.#.....#.............#.#.#.#.#...#.#.#.#...#.#...#.#.#.#...#...#...#...#.............#.#.....#...#.#.....#...#.....#...#
#.#####.#.#.#.#####.#.#.#####.#############.#.###.#.#.#.#.#.#####.#####.#.#.#.#######.#.#.#.###.#########.#.#####.###.#.#####.#.#.###.#.###.#
#.....#...#.#.....#.....#.......#.....#.....#.......#...#.#.......#...#...#...........#...#...#...#.....#.#.....#...#.#...#.....#.........#.#
#.###.#####.#####.#####.#####.###.###.#.#.#.###########.#.#.###.#.#.#.#########.#############.###.#.###.#.#####.###.#.###.#######.#######.#.#
#.#...#.....#...#...#...#...#.#...#.#.....#.....#.......#.#.#...#...#...#.....#.....#.....#.#.#...#.#...#.....#.#.....#...........#...#.#.#.#
###.###.#.###.#.#.#.#.#.#.#.###.###.#.#####.###.#.#######.###.###.#.###.#.###.#####.#.###.#.#.#.#.#.#.#####.###.#####.#.###.#.#.###.#.#.#.#.#
#.....#...........#.#.#.#.#.....#...#.......#.#.#.#.#.........#...#.#...#...#...#.....#...#.#.#.#...#.#...#...#...#...#.....#.#.#...#.#...#.#
#.###.#.###########.#.#.#.###.###.#.#######.#.#.#.#.#.#########.###.#.###.#.###.#######.###.#.#.###.#.#.#.###.###.#.#########.#.#.###.#.###.#
#...#.....#.........#.#.#.......#.#...#.....#.#.#...#.........#.....#...#.#.#.#...#...#...#.#...#...#...#...#...#.#.#.#...#...#.#.#.#.#.....#
#.#.#####.#######.###.#.#######.#.#####.#.#.#.#.#######.#.#.#.#########.###.#.###.#.#.###.#.#####.#.#######.###.#.#.#.#.#.#.###.#.#.#.#####.#
#.#.....#.#...#.......#...#...#.#.#.....#.#.#.#.........#...#.........#...#.#...#.#.#.............#.....#...#...#.#...#.#.#...#.#...#...#.#.#
#######.#.#.#.#.###.#.#####.#.#.#.#.#####.#.#.#############.#########.###.#.#.#.#.###########.#######.#.#.#.#.#.#.###.#.#.#.#.#.###.###.#.#.#
#.......#...#.#.#...#.....#.#...#...#...#.#...#.....#.....#.........#...#...#.#.#.......#...#...#.....#...#.#.#.#...#.#.#.#.#...#.#...#.#.#.#
#.###########.#.#.###.###.#.#######.#.#.#.###.#.#.#.#.###.#########.#########.#.#######.#.#####.#.#########.#.#####.###.#.#.#.#.#.###.#.#.#.#
#.#.........#...#.....#.#.#.#.....#...#.#...#...#.#.#.#.#.......#...#.......#.#...#...#.#.....#.#...#.....#.#...#...#...#.#.#.#.....#.#.#...#
#.#.#######.###.#######.#.#.#.###.#####.###.###.#.#.#.#.#######.#.###.###.#.#.###.#.#.#.#####.#.###.#.###.#.#.#.#.###.###.#.#.#######.#.###.#
#.#.#.....#...#.........#.#...#.#.#.....#...#...#.#.#...#...#...#.#...#.#...#...#...#.#.....#.....#.#.#.....#.#.#.#.......#.#.....#...#.....#
#.#.#.###.#.#####.#######.#####.#.#.#####.###.###.###.###.#.#.#.#.#.###.#.#####.#####.#.#.#.#####.#.#.#######.#.#.#.###.#########.#.#######.#
#.#.#.#.#.#.....#.#.......#...#...#.#...#.#...#.#.....#...#...#.#...#.....#.....#.#...#.#.#...#.#...#...#.....#...#.#...........#...#.......#
#.#.#.#.#.#####.#.#.#####.#.#.#.###.#.#.#.#.###.#.#####.#######.#####.#####.#.###.#.###.#.###.#.#.#####.###.#######.###########.#####.#####.#
#.#.#.#.#...#...#.#...#...#.#...#.#.#.#...#.#.........#.#...#...#...#...#.#.#...#...#...#.#...#...#...#...#.#...#.....#.#.....#...#...#...#.#
#.###.#.###.#.###.###.###.#.#####.#.#.#####.###########.###.#.###.#.###.#.#.###.#####.#.#.###.#####.#.###.#.#.#.#.###.#.#.###.###.#.###.###.#
#.......#...#...#...#...#.#...#.....#.#.#...#.....#...#...#.#...#.#.....#.....#.......#.....#.#...#.#.#...#.#.#...#...#.#.....#...#.#.....#.#
#.#######.###.#.###.#.#.#.###.###.###.#.#.###.###.#.#.#.#.#.###.#.#############.###########.#.#.#.#.#.#.###.#.#####.###.#.#.#.#.###.#####.#.#
#...#...#...#.#.....#.#.#...#.......#.#...#.....#...#.#.#.#...#.#.............#.#.........#.#...#.#.#...#...#.....#.#.....#.#.#.#.......#...#
#####.#.###.#.#######.#.###.###.#####.#.###.###.#####.#.#.###.#.#############.#.#####.###.#.#####.#.#####.###.#.#.#.###.###.###.#######.#.###
#.....#...#.#.#.......#.#.#.#.#.......#...#.#...#...#.#.....#.......#...#...#.#.......#.....#.....#.#.....#.#...#.#...#.................#...#
#.#.#####.#.#.#.#####.#.#.#.#.#########.#.#.#.###.#.#.#####.#####.#.#.###.#.#.#####.#####.#.#.#####.#.#####.#.#####.#.#####################.#
#.#.....#...#.#.#.....#.#.........#.......#.#...#.#.#.....#.......#...#...#...#...#.#...#...#.#.....#.#.......#...#.#.#...........#...#.....#
#.#.###.#####.#.###.###.#.#########.###########.#.#.#####.#.#####.#.###.#######.###.#.#.#####.#.#.###.#.#######.#.###.#.#########.#.#.#.#####
#.#.........#.#...#.#...#.#...#.....#.............#...#...#.#...#.#.#...#...........#.#...#...#.#.#.#.#...#...#.#...#...#.........#.#.#...#.#
#.#.#.#######.#.#.###.#.###.#.#.#####.###.###.#####.#.#.###.#.#.#.#.#.###.###########.###.#.#####.#.#.###.#.#.#.###.#####.#########.#####.#.#
#.#.#.#.........#.....#.#...#...#.#...#...#.......#.#.#.#...#.#.#.#.#.#.#.#...#.......#...#.......#.#...#...#.#.#.#.......#.........#.....#.#
#.#.###.#########.#.#####.#######.#.#.#.#########.###.#.#####.#.#.#.#.#.#.#.#.#.#######.###########.###.#####.#.#.#########.#.#######.###.#.#
#.#...#...........#.......#...#...#.#.#.....#...#.....#.......#.#...#.......#.#...#...#.#.........#.....#.....#.#...#.....#.#...#...#.#.....#
#.#.#.#######.#.###.#######.###.#.#.#.#####.#.#.###############.###.#.#.###.###.#.#.#.#.###.#####.#.#.###.#####.###.#.###.#.###.#.#.#.###.#.#
#.#.#.....#...#...#...#.....#...#.........#...#.#.....#.....#.#.....#...#...#.....#.#.#...#.#...#.#...#.#.#...#...#...#...#...#.......#...#.#
#.###.###.#.###.#.###.###.###.#####.###########.#.###.#.###.#.#####.###.#.###.#.###.#.###.#.#.#.#.###.#.#.#.#####.#.###.#.###.#########.#.###
#.....#...#.#...#...#...#.....#...#.#...#.......#.#.....#.#...#...#.#.#.#...#...#...#...#.#.#.#...#...#.....#.....#...#.#.#...#.........#...#
###.#.###.#.#.###.#.###.#####.#.#.###.#.#.#######.#######.###.###.#.#.#.#####.#.#.###.#.#.#.#.#.###.#########.#######.#.#.#.#########.#.#.#.#
#...#.#.....#...#.#...#.....#.#.#...#.#.#.#.....#...#...#.........#.#.#.#...#.#.#.......#.#...#.#...#.........#.#.....#.#...#.......#.#...#.#
#.###.#.#.###.#.#.#.#######.###.#.#.#.#.#.#.###.#.#.#.#.###########.#.#.#.#.###.#.#.#####.#.###.#.###.#########.#.#####.#####.#####.#.#####.#
#.#...#.#.#...#.#.#.......#.....#...#.#.#.#...#.....#.#.....#...........#.#.....#.#.....#.#.#...#.....#.........#.......#.....#...#.#.#.....#
#.#.#.#.#.#.###.#.#####.#.#######.###.#.#.#.#####.#.#.#####.#.#.#######.#.#########.###.#.#.#.#########.###############.#.###.#.###.#.#.###.#
#.#.......#.#...#.....#.#.#.......#...#.#.#.#...#.#...#...#...#...................#.#.#...#.#.....#.....#.............#.#.#.#.#.....#.#.#...#
#.#.#.###.#.#.#####.#.###.#.#######.###.#.#.#.#.#.#####.#######.#.#.#####.#####.#.#.#.#####.###.###.###.#.#######.#####.#.#.#.#.#####.#.#.###
#.....#.....#.#...#.#.#...#.....#...#.....#.#.#.#.#...#.........#.#...#.....#.....#.#.....#.#.#.......#.#.............#.#...#.#.#.......#.#.#
#.###.#.#.###.#.#.#.#.#.#######.#.#.#.#######.#.#.#.###.#######.#.###.#####.#.#####.#.###.#.#.#########.#.#.#########.#.###.#.#.#.###.###.#.#
#.....#...#...#.#.#.#.#.#.....#.#.#.#.#...#...#.#.#.#...#.....#.#...#.....#.#.#.#...#.#...#.......#.....#.#.........#...#...#...............#
#.###.###.###.#.#.###.#.#.#.#.#.#.#.###.#.#.###.#.#.#.###.#####.#########.###.#.#.###.#.#####.#####.###.#.###.###.#.#########.#####.#.#.###.#
#...............#.....#...#.#.#.#.#.#...#...#...#.#.#.....#.....#.......#.....#...#...#.......#...#.#.#.#...#.#...#...#.....#.#.....#.....#.#
#.#.#.###.#####.#######.###.###.#.#.#.#######.###.#.###.#.#.#.###.###.#####.###.###.#######.###.#.#.#.#.###.###.#####.###.#.#.#.#####.#####.#
#.#.#.....#.....#...#...#.#.....#.#.#.....#...#.#.#.......#.#.#...#.#.........#.#...#.#...#...#.#...#...#.#...#.#.........#...#...#.........#
#.#.#######.#####.#.#.###.#######.#.#####.#.###.#.#.#######.###.###.#########.#.#.###.#.#.#.###.#####.###.###.#.#.###############.#.#.#######
#...#.....#...#...#...#...........#.....#.#.......#.......#...#.#.........#.#...#.#.....#.#.#...#.....#.....#...#.......#.........#.#.......#
###.#.###.###.#.###.#.#.#######.#.###.#.#.###.#.#####.#######.#.#.#####.#.#.#####.#.###.#.###.#####.###.#.#######.#.#####.#####.#.#.#.#####.#
#...#.#.#.....#.#.#...#...#.....#...#.#...#...#.....#.#...#...#.#.#.....#...#...#...#...#...#.....#.#.............#.#.....#.#...#.#.#.....#.#
#####.#.###.###.#.#####.#.#.#######.#######.#######.###.#.#.#.#.#.#.###.#####.#.#.###.#####.#.###.#.#.###.#####.#.#.#.#####.#.#####.#####.#.#
#.....#.......#.#.....#...#.#...#.#.......#...#.....#...#...#.#.#.#.#...#.....#...#...#.....#...#...#...#.......#.#.#...#...#.....#.#.#...#.#
#.#####.###.#.#.#.#.#.#####.#.#.#.#.#.###.#.#.#.#####.###.#####.#.#.###.#.#########.###.#########.#.#.#.#.#.###.#.#.###.#.#.#####.#.#.#.###.#
#...#...#...#.#.#.#.#.....#...#.#.#.#.#.#...#.#.#.....#.......#.#.#...#.#.....#.#...#.....#.......#.......#.#...#.#...#...#.#...#...#...#...#
###.#.#.#.#.###.#.#.#####.###.#.#.#.#.#.#####.#.#.###.#.#####.#.#.###.#######.#.#.#######.#.###.#####.#####.#.###.#.#######.#.#.###.#####.#.#
#...............#.#.#...#...#.#.#.....#.........#.#...#.#.....#.#.#.#.......#...#.#...#.....#.#...........#.....#.#.....#...#...............#
#.#########.#.#.###.#.#####.###.#########.#######.#.#.#.#.#####.#.#.#######.###.#.#.#.#######.#.#######.#.#######.#####.#.#########.#.#####.#
#.#...........#.....#.....#.....#.......#.#...#...#.#.#.#.......#.#.......#...#...#.#.............#.....#.........#.....#.#.........#.....#.#
#.#.#######.#.###########.###.###.#####.#.#.#.#####.#.#.#######.#.#.#######.###.#.#.#####.#########.###############.#.#.#.###.#####.#.#.#.#.#
#.#.......#.....#.........#...#...#...#.#...#...#...#.#.#...#.......#...........#...#.....#.........#.......#.......#...#...#.#.....#...#.#.#
#.###.###.#.#####.###.#####.###.#.#.###.#######.#.#####.#.#.#.#.#####.#####.#.#######.#.#.#.###########.###.#.#############.#.#.###.#.###.#.#
#...#...#...........#.......#...#.....#...#...#...#...#...#.#.#.#.....#...#.#.#...#...#.................#...#...#.........#...#.....#.#...#.#
#.#.#######.#######.#####.###.###.###.###.#.#.#.###.#.#####.#.#.#.#####.#.#.#.#.#.#.#####.###.###.###.#####.###.#.#####.###.###.###.#.#.###.#
#.#...#.......#...#.#...#.#...#.......#.#...#.#.#...#...........................#.#...#...#...#...#...#...#.#...#.#.................#.#.#...#
#.###.#.#####.#.#.###.#.#.#.###.#.###.#.#####.#.#.#######.#.#.#.###.#.#.#####.#.#.###.#.#.###.#.#######.#.###.#.#.#.#.###.###.#.#.#.#.#.###.#
#...#...#...#...#.#...#.#.#.#...#...............#...#...#...#.#.....#...#...#.#.#...#.#.....#.#.....#...#.....#.#.#.#...#.....#.#...#.#...#.#
###.#####.#.#####.#.###.#.#.#.#.#####.#####.#.#.###.#.#.#####.#.#####.###.#.#.#.#####.###.#.#.#####.#.#####.#####.#.#####.#####.#.#.#####.###
#...#.....................#.#.#.#...#.#...#.#.#.#...#.#.......................#.#...#.....#.............#...#.....#...#.......#.#.#.....#...#
#.#####.###.#.#.#.###.#.#.#.#.#.#.#.###.#.###.###.###.#.#####.#.#.###.#######.#.#.#.###.#.#.#####.#.###.#.###.#######.#.#.#.###.#.#.#.#.#.#.#
#...................#.#.#.#.#.#...#.....#.#...#.....................#.#.......#.#.#.....#.#.#...#.#...#.#.#...#.....#...#.#.#...#.....#.#.#.#
#########.###.#.#.###.#.###.#############.#.###.###.#######.#.#.#.#.#.#.#######.#.###.###.#.#.#.###.###.#.#.###.###.#####.#.#.#.#######.###.#
#.....#...#...#.#.#...#...#.#...#...#.....#.#...#...#.....#.#.....#.#.#.#.....#.#.#...#.....#.#.....#...#.#.#...#.#...#...#.#...#.....#.....#
#.###.#.#####.#.#.#.#####.#.#.#.#.#.#.###.#.#.###.###.###.#.#.#.#.#.###.###.#.#.#.#####.#.###.#####.#.#####.###.#.###.#.#.#.###.#.#.###.###.#
#S..#.........#.........#.....#...#...#...#...#.......#...#.......#.........#...#.............#...............................#...#.........#
#############################################################################################################################################"""

def parse_input(input):
    maze = [list(line) for line in input.strip().split("\n")]
    start, end = None, None

    width, height = len(maze[0]), len(maze)

    for y in range(height):
        for x in range(width):
            if maze[y][x] == "S":
                start = (x, y)
            if maze[y][x] == "E":
                end = (x, y)
    
    return maze, start, end

def dijkstra(maze, start, end, previous):
    width, height = len(maze[0]), len(maze)
    
    # East, South, West, North
    directions = [(1,0), (0,1), (-1, 0), (0, -1)]

    # x, y, facing (start facing east (idx 0))
    current_state = (start[0], start[1], 0)

    # score, current_state, [states]
    pq = [(0, current_state, [current_state])] 
    visited = {}

    while pq:
        score, current_state, states = heapq.heappop(pq)
        x, y, facing = current_state

        if (x, y) == end:
            return score, states

        if (x, y, facing) in visited and visited[(x, y, facing)] <= score:
            continue
        visited[(x, y, facing)] = score

        dx, dy = directions[facing]
        nx, ny = x + dx, y + dy

        if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != "#":
            new_states = states + [(nx, ny, facing)]
            if (nx, ny) == end and states + [(nx, ny, facing)] in previous:
                heapq.heappush(pq, (score + 1000000, (nx, ny, facing), new_states))
            else:
                heapq.heappush(pq, (score + 1, (nx, ny, facing), new_states))
        
        left_facing = (facing - 1) % 4
        new_states = states + [(x, y, left_facing)]
        heapq.heappush(pq, (score + 1000, (x, y, left_facing), new_states))

        right_facing = (facing + 1) % 4
        new_states = states + [(x, y, right_facing)]
        heapq.heappush(pq, (score + 1000, (x, y, right_facing), new_states))
    
    return float('inf'), []


def print_best_tiles(maze, tile_set):    
    width, height = len(maze[0]), len(maze)

    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in tile_set:
                line += " O "
            else:
                line += f" {maze[y][x]} "
        print(line)

def simulate(input):
    maze, start, end = parse_input(input)

    score = 0
    previous = []

    min_score, states = dijkstra(maze, start, end, [])
    previous.append(states)

    while score <= min_score:
        
        score, states = dijkstra(maze, start, end, previous)
        if score > min_score:
            break
        previous.append(states)
    
    tile_set = set()
    for states in previous:
        for x, y, _ in states:
            tile_set.add((x, y))

    print_best_tiles(maze, tile_set)
    print(len(tile_set))

simulate(t_data)