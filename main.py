import random
import time
import gene
import level
import machine


random.seed()
start_time = time.time()

main_level = level.generate(10)
pool = gene.process_pool(gene.generate_pool(), main_level)

evolve_cycles = 256
for i in range(evolve_cycles):
    pool = gene.process_pool(gene.generate_new_pool(pool), main_level)
    if i % 64 == 0:
        print(i, " => ", gene.count_fitness_sum(pool) / len(pool))

max_fitness = 0
gene = None
for gene_fitness in pool:
    if gene_fitness[1] > max_fitness:
        max_fitness = gene_fitness[1]
        gene = gene_fitness[0]

print("evolved", 256, "cycles in",
      round(time.time() - start_time, 2), "seconds")
print()

print("result:")
level.print_level(main_level)
for step in machine.interpret(gene):
    print(step, end="")
print()
