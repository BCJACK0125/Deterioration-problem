
import numpy as np

def simulate_replacement_cost(failure_prob_initial, failure_prob_increase, replacement_cost, num_simulations):
    """
    Simulates the replacement cost of a system over a given number of simulations.
    
    Args:
        failure_prob_initial (float): The initial failure probability of the system.
        failure_prob_increase (float): The increase in failure probability per unit of age.
        replacement_cost (float): The cost of replacing the system.
        num_simulations (int): The number of simulations to run.
    
    Returns:
        float: The long-run average replacement cost.
    """
    total_cost = 0
    age = 0
    
    # Simulate the system
    for _ in range(num_simulations):
        if np.random.rand() <= failure_prob_initial + failure_prob_increase * age:
            total_cost += replacement_cost
            age = 0
        else:
            age += 1
    
    # Calculate the long-run average replacement cost
    average_cost = total_cost / num_simulations
    
    return average_cost

np.random.seed(0)
failure_prob_initial = 0.1
failure_prob_increase = 0.01
replacement_cost = 1
num_simulations = 10000000

average_cost = simulate_replacement_cost(failure_prob_initial, failure_prob_increase, replacement_cost, num_simulations)
print("Long-run average replacement cost:", average_cost)