# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Name: 
# ---------------------------------------
# How many dice do you have to roll in order to
# optimize the probability of rolling exactly 2 sixes?
# ---------------------------------------

import random

# Contant representing the number of times you want to run the simulation
# After your code works, change this number to ten million for a (better) answer
simulation_number = 100

# ---------------------------------------
# rolls_a_six
# ---------------------------------------
# 
# ---------------------------------------
# Simulates a die roll where 1-6 are equally probable
# Returns a Bool (True if the value is 6 and False otherwise)
# ---------------------------------------

""" The missing rolls_a_six function goes here ... """


# ---------------------------------------
# roll_2_sixes_given_n_dice(num_dice)
# ---------------------------------------
# num_dice: the number of dice rolled, an integer
# ---------------------------------------
# Rolls n dice, counts number of times two 6's occured, returns [True if exactly two 6's, else if False]
# Returns a Bool, whether rolling n dice produced two 6's
# ---------------------------------------

""" The missing roll_2_sixes_given_n_dice function goes here ... """

# ---------------------------------------
# simulate_prob_2_sixes_given_n_dice
# ---------------------------------------
# num_dice: the number of dice rolled, an integer
# num_rolls: the number of times you roll num_dice dice, an integer
# ---------------------------------------
# Loops num_rolls times, counts the number of times two 6s occurred given num_dice dice, returns the probability of rolling two 6s given num_dice dice
# Returns a float, the probability of rolling two 6s given num_dice dice over num_rolls events
# ---------------------------------------

""" The missing simulate_prob_2_sixes_given_n_dice function goes here ... """

# ---------------------------------------
# main - controls the main flow of logic
# ---------------------------------------

def main():
    print("{:10}{:10}".format("Dice", "Probability of Rolling 2 Sixes"))
    print("{:10}{:10}".format("------", "------"))
    for i in range(2,21):
        str_i = str(i)
        str_prob = str(simulate_prob_2_sixes_given_n_dice(i,simulation_number))
        print("{:10}{:10}".format(str_i, str_prob))
# ---------------------------------------

main()
           
