# An accounting system models a revenue transaction t as an object with two
# attributes, t.date and t.amount representing the date and amount of the
# transaction, respectively. Dates are represented as numbers of days since
# a reference initial date, such that t2.date − t1.date is the number of days
# between transactions t1 and t2. Amounts are positive numbers. With that,
# consider the following algo_x(T) that takes an array T of transactions:
# Explain what it does
# Analyze complexity
# Write a strictly better algorithm


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort
from random import shuffle


class Transaction():
    def __init__(self, amount: int, date: int):
        self.amount = amount
        self.date = date


# Calculates the most amount of sales of sets of transactions that happened
# between 10 days, thus the most amount of sales that happened in a 10 days range
# Complexity: O(n^2)
def algo_x(T: list[Transaction]):
    x = 0
    for i in range(len(T)):
        l = T[i].amount
        r = T[i].amount
        for j in range(len(T)):
            if i != j:
                if T[j].date <= T[i].date and T[i].date - T[j].date <= 10:
                    l = l + T[j].amount
                if T[j].date >= T[i].date and T[j].date - T[i].date <= 10:
                    r = r + T[j].amount

        if x < r:
            x = r
        if x < l:
            x = l
    return x


# Complexity: O(n*log(n))
def better_x(T):
    T.sort(key=lambda x: x.date)
    i = 0
    j = 0
    v = 0
    m = 0

    while j < len(T):
        if T[j].date - T[i].date <= 10:
            v = v + T[j].amount
            j += 1

            if m < v:
                m = v
        else:
            v = v - T[i].amount
            i += 1

    return m


if __name__ == "__main__":
    T = [
        Transaction(10, 15),
        Transaction(10, 16),
        Transaction(10, 4),
        Transaction(10, 24),
        Transaction(10, 40),
        Transaction(10, 10),
        Transaction(10, 41)
    ]

    print(algo_x(T))
    print(better_x(T))

    # Benchmark
    algo_durations = []
    better_durations = []

    inputs = []
    for i in range(1, 501):
        inputs.append([])

        for j in range(i):
            inputs[-1].append(Transaction(np.random.randint(
                0, 10, dtype=int), np.random.randint(0, i + 1, dtype=int)))

    for inp in inputs:
        tStart = time.perf_counter()
        algo_x(inp)
        tEnd = time.perf_counter()

        algo_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        better_x(inp)
        tEnd = time.perf_counter()

        better_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 500)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, algo_durations, label='algo_x O(n^2)')
    plt.plot(x, better_durations, label='better_x O(n*log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'algo_x vs better_x 288')

    plt.legend()
    plt.show()
