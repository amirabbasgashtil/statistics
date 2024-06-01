import numpy as np

def random_probability():
    return(np.random.uniform(0, 1))


P_A = random_probability()
P_B = random_probability()
# for A and B suppose to be independent.
P_AandB = P_A * P_B     # probability of A and B
P_AlB = P_AandB / P_B   # P(A|B)
P_BlA = P_AandB / P_A   # P(B|A)

print(P_AlB)

P_AlB = P_A * P_BlA / P_B  #bayes theorem

print(P_AlB)
