"""
This script calculates the stationary distribution of a Markov chain using the power iteration method.
The Markov chain has 91 states represented by the list V, where V[0] is the initial state and V[1] to V[90] are the subsequent states.
The stationary distribution is computed by iterating through the equations and updating the values of V until convergence.
The final stationary distribution is outputted with 4 decimal places.
The sum of the values in V weighted by the state values is also calculated and displayed.
"""

V = [1] + [0] * 90  # initialize V list with 91 elements and set all values to 0

for k in range(10000):
    newV = [0] * 91  # create a new list to store the updated values of V

    # compute V[0] using the first equation
    for i in range(91):
        newV[0] += (0.1 + 0.01 * i) * V[i]

    # compute V[i] for i = 1 to 90 using the second equation
    for i in range(1, 91):
        newV[i] = (0.9 - (i - 1) * 0.01) * V[i - 1]

    V = newV  # update V with the new values

print([f"{v:.4f}" for v in V])  # output the final stationary distribution with 4 decimal places

# sum up the values in V with weight
total = 0
for i in range(91):
    total += V[i] * (0.1 + 0.01*i)

print(f"The sum of the values in V is {total:.5f}")

