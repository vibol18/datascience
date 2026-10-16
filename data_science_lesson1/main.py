import pandas as pd
import numpy as np
score = pd.array([10,23,65,23])
# print(f"Your Array is ${score}")
print(score)
print("Average",np.mean(score))
# mean is using for average

print("median",np.median(score))
#median average of 2 center 
# wrong more value they call it Outlier
from collections import Counter

scores = [70, 80, 80, 90, 80, 100]

counts = Counter(scores)

print("Mode:", counts.most_common(1)[0][0])
print("Standard Deviation:", np.std(scores))