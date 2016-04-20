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
print("finished in", round(time.time() - start_time, 2), "seconds")
