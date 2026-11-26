import random


# Calculate the exact birthday probability
def exact_probability(group_size):
    days = 365

    # More than 365 people guarantees a shared birthday
    if group_size > days:
        return 1.0

    probability_different = 1.0

    for i in range(group_size):
        probability_different *= (days - i) / days

    probability_match = 1 - probability_different

    return probability_match



# Simulate the Birthday Problem
def simulate_birthday(group_size, trials):
    successful_groups = 0

    for trial in range(trials):

        # Generate random birthdays for each person
        birthdays = []

        for person in range(group_size):
            birthday = random.randint(1, 365)
            birthdays.append(birthday)

        # Check for at least one matching birthday
        if len(birthdays) != len(set(birthdays)):
            successful_groups += 1

    simulated_probability = successful_groups / trials

    return successful_groups, simulated_probability



# Find the minimum group size
def find_minimum_group_size():
    group_size = 1

    while exact_probability(group_size) <= 0.5:
        group_size += 1

    return group_size


# MAIN PROGRAM
print("\n\tBIRTHDAY PROBLEM SIMULATION")

# Find Exact probability for 23 people
group_size = 23

exact_result = exact_probability(group_size)

print("\nPART 1: EXACT PROBABILITY")
print("Group size:", group_size)
print("Exact probability:", exact_result)
print("Percentage:", exact_result * 100, "%")


# Simulation using 500 trials
trials = 500

successful_groups, simulated_result = simulate_birthday(
    group_size, trials
)

print("\nPART 2: MONTE CARLO SIMULATION")
print("Number of trials:", trials)
print("Groups with shared birthdays:", successful_groups)
print("Simulated probability:", simulated_result)
print("Percentage:", simulated_result * 100, "%")


# Find minimum group size
minimum_size = find_minimum_group_size()

print("\nPART 3: MINIMUM GROUP SIZE")
print("Minimum group size:", minimum_size)

minimum_exact = exact_probability(minimum_size)

print("Exact probability:", minimum_exact)
print("Percentage:", minimum_exact * 100, "%")


# Confirm the result through simulation
minimum_hits, minimum_simulated = simulate_birthday(
    minimum_size, trials
)

print("\nSIMULATION CONFIRMATION")
print("Number of trials:", trials)
print("Successful groups:", minimum_hits)
print("Simulated probability:", minimum_simulated)
print("Percentage:", minimum_simulated * 100, "%")


# Bouns Challange: Calculate the birthday probability for different group sizes
print("\nBONUS: Birthday Probability by Group Size")

group_sizes = [5, 10, 15, 20, 22, 23, 30, 40, 50]

for size in group_sizes:
    probability = exact_probability(size)

    print(f"{size} people: {probability * 100:.2f}%")


