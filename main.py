import random
import gene
import level
import machine


random.seed()

main_level = level.generate(10)

pool = gene.process_pool(gene.generate_pool(), main_level)
for i in range(500):
    pool = gene.process_pool(gene.generate_new_pool(pool), main_level)
    print(i, " => ", gene.count_fitness_sum(pool) / len(pool))

max_fitness = 0
gene = None
for gene_fitness in pool:
    if gene_fitness[1] > max_fitness:
        max_fitness = gene_fitness[1]
        gene = gene_fitness[0]

level.print_level(main_level)
for step in machine.interpret(gene):
    print(step, end="")
print()
