def ones(num: int):
    """Get all one bits from a number"""

    bit = 1
    while num >= bit:
        if num & bit:
            yield bit
        bit <<= 1


def interpret(gene: bytes, max_iterations: int = 500):
    """Interpret the gene in the virtual machine
       and return moving directions"""

    memory = bytearray(gene)
    result = []
    i, iter = 0, 0

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
            ones_number = len(list(ones(byte)))
            if ones_number <= 2:
                result.append("H")
            elif ones_number <= 4:
                result.append("D")
            elif ones_number <= 6:
                result.append("P")
            else:
                result.append("L")

        i = 0 if i >= len(gene) - 1 else i + 1
        iter += 1
        if iter >= max_iterations:
            break

    return tuple(result)


def run(sequence: tuple, level: tuple, start: tuple = (0, 0)):
    """Run the sequence on a map"""

    pos = start
    fitness = 0

    for dir in sequence:
        if dir == "H":
            pos = (pos[0], pos[1] - 1)
        elif dir == "R":
            pos = (pos[0] + 1, pos[1])
        elif dir == "D":
            pos = (pos[0], pos[1] + 1)
        else:
            pos = (pos[0] - 1, pos[1])

        if pos[0] < 0 or pos[0] >= len(level) or pos[1] < 0 or pos[1] >= len(level):
            print("Moved out of the level!")
            break
        else:
            if level[pos[1]][pos[0]] > 0:
                print("OMG treasure!!!")
                fitness += 1000

        fitness -= 1

    return fitness
