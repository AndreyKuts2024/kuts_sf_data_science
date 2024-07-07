""" Game guess the number"""

import numpy as np

number = np.random.randint(1, 101) # We make a number

# number of attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100"))
    if predict_number > number:
        print("The number must be less then!")
        
    elif predict_number < number:
        print("The number must be greater then!")
        
    else:
        print(f"You guessed the number in {count} attempts! This is the number = {number}")
        break # End of the game, exit the loop
    
        
        
        