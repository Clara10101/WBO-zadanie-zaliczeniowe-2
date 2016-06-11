"""
Wywolanie funkcji tree z pliku tree.py z wykorzystaniem biblioteki multiprocessing,
program sprawdza liczbe rdzeni i wielowatkowo wywoluje funkcje, konieczne aby przyspieszyc kilkugodzinne obliczenia
"""

import subprocess
import multiprocessing
from tree import tree

if __name__ == '__main__':

    numProcessors = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(numProcessors)

    i = 1
    grupa = 1
    tasks = []

    while i < 4208:
        tasks.append((i,i+50,grupa))
        i += 50
        grupa += 1
    tasks.append((4201, 4208))

    # Run tasks
    results = [pool.apply_async( tree, t ) for t in tasks]

    # Process results
    for i, result in enumerate(results):
        print("Result for cluster %d written to phyi file" % (i))

    pool.close()
    pool.join()
