def ones(num: int):
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

    return result
