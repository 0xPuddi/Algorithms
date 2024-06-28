
import time
import numpy as np
import matplotlib.pyplot as plt


# Not efficient exp of random x
def exp_linear(x, k):
    if k == 0:
        return 1

    exp = x
    for i in range(1, k):
        exp = exp * x

    return exp


# Efficient exp (Multiply and Square algorithm) of 2
def exp_two_logarithm(k):
    if k == 0:
        return 1

    b = bin(k)
    exp = exp_linear(2, int(b[2]))
    exp = exp * exp
    for i in range(3, len(b)):
        e = exp_linear(2, int(b[i]))

        if i == len(b) - 1:
            exp = exp * e
            break
        exp = exp_linear(exp * e, 2)

    return exp


if __name__ == "__main__":
    print(exp_linear(100, 0))
    exp_linear(2, 4000)
    exp_two_logarithm(4000)

    # Benchmark
    exp_linear_durations = []
    exp_two_logarithm_durations = []

    inputs = []
    for i in range(0, 4000):
        inputs.append(i)

    for inp in inputs:
        tStart = time.perf_counter()
        exp_linear(2, inp)
        tEnd = time.perf_counter()

        exp_linear_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        exp_two_logarithm(inp)
        tEnd = time.perf_counter()

        exp_two_logarithm_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 4000)]  # Range from 0 to 1000

    # Plot array1 and array2
    plt.plot(x, exp_linear_durations, label='Exp of two Linear')
    plt.plot(x, exp_two_logarithm_durations, label='Exp of two Logarithm')

    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'lol')

    plt.yscale("log")
    plt.legend()
    plt.show()
