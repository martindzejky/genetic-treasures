def interpret(instruction_set, max_iterations=500):
    """ Runs the instruction set in a virtual machine. Returns the printed path. """

    def make_dir(from_byte):
        if from_byte < 64:
            return 'U'
        elif from_byte < 128:
            return 'R'
        elif from_byte < 192:
            return 'D'
        else:
            return 'L'

    # prepare the memory, the instruction pointer, and the result
    ip = 0
    memory = list(instruction_set)
    result = []

    for iteration in range(max_iterations):
        # get the instruction and the pointer
        byte = memory[ip]
        instruction = byte >> 6
        pointer = byte & int('00111111', 2)

        # bind the pointer to the memory
        pointer %= len(memory)

        # evaluate the instruction
        if instruction == 0:
            # increase byte
            memory[pointer] = 0 if memory[pointer] >= 255 else memory[pointer] + 1
        elif instruction == 1:
            # decrease byte
            memory[pointer] = 255 if memory[pointer] <= 0 else memory[pointer] - 1
        elif instruction == 2:
            # jump to byte
            ip = pointer
        elif instruction == 3:
            # print direction
            result.append(make_dir(memory[pointer]))

        # move to the next byte, or to the start if out of range
        # only move if we did not jump
        if instruction != 2:
            ip += 1
        if ip >= len(memory):
            ip = 0

    return result
