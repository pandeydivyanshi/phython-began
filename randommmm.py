import random
print( random.random() )                                                              # Random number between 0.0 and 1.0
print("Random integer between 1 and 10:", random.randint(1, 10))                      # Random integer between 1 and 10
print("Random number from range(1, 10, 5):", random.randrange(1, 10, 5))              # Random number from range(1, 10, 5)
print("Random number from range(100, 1000, 100):", random.randrange(100, 1000, 100))  # Random number from range(100, 1000, 100)
print("Random choice from list [1, 2, 3, 4, 5]:", random.choice([1, 2, 3, 4, 5]))      # Random choice from list
print(random.uniform(1.0, 10.0))                                                      # Random float between 1.0 and 10.0
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice from a list of strings
print(random.shuffle([1, 2, 3, 4, 5]))  # Shuffle a list in place
print(random.sample([1, 2, 3, 4, 5], 3))  # Random sample of 3 elements from a list
print(help(random))                                                # Display help for the random module
print(help(random.uniform))  # Display help for the random.uniform function