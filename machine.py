def interpret_inset(inset):
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

    # TODO: run the machine
    return tuple(map(make_dir, inset))


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
