import time
import random
import evolution


print("starting the evolution")
print()
start_time = time.time()

random.seed()
evolution.run()

print()
print("finished in", round(time.time() - start_time, 2), "seconds")
