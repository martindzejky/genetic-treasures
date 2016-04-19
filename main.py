import random
import gene
import level


random.seed()

main_level = level.generate(7)
print("~~~~LEVEL~~~~")
level.print_level(main_level)
print("~~~~~~~~~~~~~")
print()

pool = gene.generate_pool()
pool_with_fitness = gene.process_pool(pool, main_level)
