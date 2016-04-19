import random
import machine
import level


random.seed()

gene = bytes([random.getrandbits(8) for x in range(64)])
main_level = level.generate(7)

print("LEVEL")
level.print_level(main_level)
print()

print("INTERPRET & RUN")
print(machine.run(machine.interpret(gene), main_level))
