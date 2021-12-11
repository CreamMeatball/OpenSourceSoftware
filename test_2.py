import numpy as np
entropy = []

p  = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
q1 = np.array([0.2, 0.2, 0.2, 0.2, 0.1, 0.1])
q2 = np.array([0.3, 0.3, 0.1, 0.1, 0.1, 0.1])
q3 = np.array([0.4, 0.2, 0.1, 0.1, 0.1, 0.1])
q4 = np.array([0.5, 0.1, 0.1, 0.1, 0.1, 0.1])

# entropy.append(sum(-p*np.log2(p))) # 1.922...
# entropy.append(sum(-q1*np.log2(q1))) # 1.922...
# entropy.append(sum(-q2*np.log2(q2))) # 1.922...
# entropy.append(sum(-q3*np.log2(q3))) # 1.922...
entropy.append(sum(-q4*np.log2(q4))) # 1.922...
print(entropy)
