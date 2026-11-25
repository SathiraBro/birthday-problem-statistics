people = 23
days = 365

probability_different = 1.0

for i in range(people):
    probability_different *= (days - i) / days

probability_match = 1 - probability_different

print("Number of people:", people)
print("Probability of all different birthdays:", probability_different)
print("Probability of a shared birthday:", probability_match)
print("Percentage:", probability_match * 100)
