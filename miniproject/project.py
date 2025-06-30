# project.py
import statistics as stat

user_input = input("Enter numbers separated by commas: ")  # e.g. 1,2,3,4

# Convert input string to a list of integers
my_list = [int(x.strip()) for x in user_input.split(",")]

# Calculations
print("List:", my_list)
print("Sum:", sum(my_list))
print("Mean:", stat.mean(my_list))
print("Mode:", stat.mode(my_list))
print("Median:", stat.median(my_list))
print("Standard Deviation:", stat.stdev(my_list))
print("Variance:", stat.variance(my_list))
print("Minimum:", min(my_list))
print("Maximum:", max(my_list))
print("Range:", max(my_list) - min(my_list))
print("Sorted List:", sorted(my_list))
print("population Variance:", stat.pvariance(my_list))
print("population Standard Deviation:", stat.pstdev(my_list))
print("count:", len(my_list))
print("Geometric Mean:", stat.geometric_mean(my_list))
print("Harmonic Mean:", stat.harmonic_mean(my_list))
print("quantiles:", stat.quantiles(my_list, n=4))  # Quartiles