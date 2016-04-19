def ones(num):
    """Count the number of 1 bits in a number"""

    bit = 1
    count = 0
    while num >= bit:
        if num & bit:
            count += 1
        bit <<= 1

    return count


def interpret(gene, max_iterations=500):
    """Interpret the gene in the virtual machine
       and return moving directions"""

    memory = list(gene)
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
            ones_number = ones(byte)
            if ones_number < 2:
                yield "H"
            elif ones_number < 4:
                yield "D"
            elif ones_number <= 6:
                yield "P"
            else:
                yield "L"

        i = 0 if i >= len(memory) - 1 else i + 1
        iter += 1
        if iter >= max_iterations:
            break


def run(sequence, level, start=(0, 0)):
    """Run the sequence on a map"""

    pos = start
    fitness = 501
    treasures = set()

    for dir in sequence:
        if dir == "H":
            pos = (pos[0], pos[1] - 1)
        elif dir == "R":
            pos = (pos[0] + 1, pos[1])
        elif dir == "D":
            pos = (pos[0], pos[1] + 1)
        else:
            pos = (pos[0] - 1, pos[1])

        fitness -= 1

        if (pos[0] < 0 or pos[0] >= len(level) or
                pos[1] < 0 or pos[1] >= len(level)):
            break
        else:
            if level[pos[1]][pos[0]] > 0:
                if pos not in treasures:
                    fitness += 1000
                    treasures.add(pos)

    return fitness
