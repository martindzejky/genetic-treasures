import time
import random
import level
import evolution
import machine


print("starting the evolution")
print()
start_time = time.time()

random.seed()
world = level.generate()
best_pair = evolution.run(world, (0, 0))

print()
print("finished in\033[36m",
      round(time.time() - start_time, 2),
      "\033[0mseconds")
print()

print("best fitness is\033[36m", best_pair[0], "\033[0m")
printable_world = machine.make_printable_level(
    world, machine.interpret_inset(best_pair[1]), (0, 0))
for y in printable_world:
    for x in y:
        print(x, "", end="")
    print()
