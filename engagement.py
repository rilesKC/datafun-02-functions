import statistics

# the two data sets
data_A = [10,11,14,20,20,20,22,24,28,31]
data_B = [2,9,13,14,20,20,24,26,32,40]

# output the results
print("\nCentral Tendency")
print("Mean: Dataset A = ", statistics.mean(data_A), "; Dataset B = ", statistics.mean(data_B))
print("Median: Dataset A = ", statistics.median(data_A), "; Dataset B = ", statistics.median(data_B))
print("Mode: Dataset A = ", statistics.mode(data_A), "; Dataset B = ", statistics.mode(data_B))
print("\nDispersion")
print(f"Variance: Dataset A = ", round(statistics.variance(data_A), 3), "; Dataset B = ", round(statistics.variance(data_B),3))
print(f"Std Dev: Dataset A = ", round(statistics.stdev(data_A), 3), "; Dataset B = ", round(statistics.stdev(data_B),3))