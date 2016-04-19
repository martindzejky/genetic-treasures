from machine import interpret
import random


random.seed()
gene = bytes([random.getrandbits(8) for x in range(64)])

print(interpret(gene))
