import numpy as np

def solve_poisson_equation():
    """
    Solves the Poisson equation using numpy.linalg.solve.

    Returns:
    X (ndarray): The solution to the Poisson equation.
    """
    Poisson_equation = np.zeros((91, 91), dtype=float)
    r = np.arange(0, 91, dtype=float)

    for i in range(91):
        Poisson_equation[i, i] = -0.9 + 0.01 * i
        Poisson_equation[i, 90] = 1
        if i > 0:
            Poisson_equation[i, i - 1] = 1
        r[i] = 0.1 + 0.01 * i

    # Solve the equation
    X = np.linalg.solve(Poisson_equation, r)

    np.set_printoptions(precision=3)
    print("The average-cost Poisson equation is:", X[90])

    return X

solve_poisson_equation()

