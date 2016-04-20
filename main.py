import time
import random
import level
import evolution


print("starting the evolution")
print()
start_time = time.time()

random.seed()
world = level.generate()
evolution.run(world, (0, 0))

print()
print("finished in\033[36m",
      round(time.time() - start_time, 2),
      "\033[0mseconds")
