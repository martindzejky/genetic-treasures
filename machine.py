def interpret_inset(inset, max_iterations=500):
    """Run the instructions in a virtual machine and
       return the directions to build a path."""

    def make_dir(byte):
        if byte < 64:
            return (-1, 0)
        elif byte < 128:
            return (0, -1)
        elif byte < 192:
            return (1, 0)
        else:
            return (0, 1)

    i, counter = 0, 0
    memory = list(inset)
    result = []

    while True:
        byte = memory[i]
        instruction = byte >> 6
        rest = byte & int("00111111", 2)

        if instruction == 0:
            memory[rest] = 0 if memory[rest] >= 255 else memory[rest] + 1
        elif instruction == 1:
            memory[rest] = 255 if memory[rest] <= 0 else memory[rest] - 1
        elif instruction == 2:
            i = rest
        elif instruction == 3:
            result.append(make_dir(memory[rest]))

        i = 0 if i >= len(memory) - 1 else i + 1
        counter += 1
        if counter >= max_iterations:
            break

    return result


def run_path(level, path, start):
    """Run the path in the level, find treasures
       and calculate a fitness value."""

    pos = start
    fitness = 1
    level = list(map(lambda x: list(x), level))
    level[pos[1]][pos[0]] = 0

    for dir in path:
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        fitness -= 1

        if pos[1] < 0 or pos[1] >= len(level):
            break
        if pos[0] < 0 or pos[0] >= len(level[0]):
            break

        if level[pos[1]][pos[0]] > 0:
            level[pos[1]][pos[0]] = 0
            fitness += 1000

    return max(1, fitness)


def make_printable_level(level, path, start):
    """Make a level with the visible path."""

    pos = start
    level = list(map(lambda x: list(x), level))
    level[pos[1]][pos[0]] = "S"

    for dir in path:
        pos = (pos[0] + dir[0], pos[1] + dir[1])

        if pos[1] < 0 or pos[1] >= len(level):
            break
        if pos[0] < 0 or pos[0] >= len(level[0]):
            break

        if level[pos[1]][pos[0]] == 0:
            if dir == (-1, 0):
                level[pos[1]][pos[0]] = "<"
            elif dir == (0, -1):
                level[pos[1]][pos[0]] = "^"
            elif dir == (1, 0):
                level[pos[1]][pos[0]] = ">"
            else:
                level[pos[1]][pos[0]] = "v"

    return level
