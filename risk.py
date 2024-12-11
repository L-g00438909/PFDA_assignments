import numpy as np
import matplotlib.pyplot as plt

# Function to roll a die a specified number of times
def roll_dice(num_rolls=1):
    """
    Rolls a die a specified number of times.
    """
    rng = np.random.default_rng()
    rolls = rng.integers(1, 7, size=num_rolls)
    return rolls

# Function to simulate a battle between one attacker and one defender
def check_winner(attacker_number, defender_number):
    """
    Function to compare a single attacker's roll vs a single defender's roll
    and return the losses for both sides.
    """
    attacker_losses = 0
    defender_losses = 0
    if attacker_number > defender_number:
        defender_losses += 1  # Defender loses a troop
    elif attacker_number < defender_number:
        attacker_losses += 1  # Attacker loses a troop
    else:  # If it's a tie, attacker loses a troop by default
        attacker_losses += 1
    return attacker_losses, defender_losses

# Function to simulate the battle with arbitrary army sizes
def simulate_battle(attacker_troops, defender_troops, num_rounds=1000):
    attacker_losses_history = []
    defender_losses_history = []
    
    round_number = 0
    while attacker_troops > 0 and defender_troops > 0 and round_number < num_rounds:
        round_number += 1
        # Calculate how many dice the attacker and defender roll
        attacker_rolls = min(3, attacker_troops)  # Attacker rolls up to 3 dice
        defender_rolls = min(2, defender_troops)  # Defender rolls up to 2 dice

        # Roll the dice for both sides
        attacker_dice = roll_dice(attacker_rolls)
        defender_dice = roll_dice(defender_rolls)

        # Sort the dice rolls in descending order
        sorted_attacker = np.sort(attacker_dice)[::-1]
        sorted_defender = np.sort(defender_dice)[::-1]

        # Compare the highest dice rolls
        for i in range(min(attacker_rolls, defender_rolls)):
            attacker_losses, defender_losses = check_winner(sorted_attacker[i], sorted_defender[i])
            attacker_troops -= attacker_losses
            defender_troops -= defender_losses

        # Store the history of losses for plotting
        attacker_losses_history.append(attacker_troops)
        defender_losses_history.append(defender_troops)

        # If either side runs out of troops, break out of the loop
        if attacker_troops <= 0 or defender_troops <= 0:
            break
    
    return attacker_losses_history, defender_losses_history, attacker_troops, defender_troops

# Simulate a battle with arbitrary army sizes
initial_attacker_troops = 200
initial_defender_troops = 200

attacker_losses_history, defender_losses_history, final_attacker_troops, final_defender_troops = simulate_battle(initial_attacker_troops, initial_defender_troops)

# Plot the results with an area plot
plt.figure(figsize=(10, 6))

# Area plot for attacker and defender
plt.fill_between(range(len(attacker_losses_history)), attacker_losses_history, color='blue', alpha=0.5, label='Attacker Troops')
plt.fill_between(range(len(defender_losses_history)), defender_losses_history, color='red', alpha=0.5, label='Defender Troops')

# Adding labels and title
plt.xlabel('Rounds')
plt.ylabel('Troops Remaining')
plt.title('Battle Simulation: Troops Remaining Over Time')

# Show legend
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()

# Print final result
print(f"\nAfter the battle:\nAttacker has {final_attacker_troops} troops left.")
print(f"Defender has {final_defender_troops} troops left.")
if final_attacker_troops > 0:
    print("The Attacker wins!")
else:
    print("The Defender wins!")
