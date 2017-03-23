# Genetic Treasures

This python program uses genetic algorithm to evolve an instruction set for a virtual machine that
executes them and creates a set of movement instructions for a guy that collects treasures on a
map. Get it? Okay, again.

## Task

We use genetic algorithm to evolve a set of instructions – 64 bytes. 1 instruction is one byte. The
first 2 bits determine the type of instruction:

- 0 = increment
- 1 = decrement
- 2 = jump
- 3 = print

The remaining 6 bits point to an instruction in the set that is to be affected. This means that the
program is self-modifying.

A virtual machine takes these instructions, evaluates them, and generates a set of movements – up,
right, down, left. This movements are generated using the print instruction.

Then there's a map with treasures and a greedy guy that wants to collect them. He takes the
generated set of movements and moves around the level. He collects a treasure when they are on the
same tile. The number of treasures collected is the fitness function for the evolution algorithm.

