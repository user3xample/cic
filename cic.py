#!/usr/bin/python3
#==============================================================================
# Title          : Compound interest calculator (CIC)
# Git            : https://github.com/user3xample/cic
# Author         : User3xample
#
# Date           : AUG 2021
#==============================================================================
# Version        : 0.1.0
# Language       : Python3
# Licence        : For personal use only. non comercial
#==============================================================================
# Description    : Compound interest calculator
# Notes          : A work in progress still, take with a pinch of salt.
#                
# Usage          : $sudo python3 cic.py
#==============================================================================


# start
# import modules # OS- for screen clearing, time - for sleep ability.
import os , time
##

# Clear the screen function
def clear_screen():  # function we can use later that clears terminal
    os.system('cls||clear')
##

# variables- These will be updated in the script leave alone.
coin = "Sterling"  # Debated weather to make this a user choice but kept fixed. Maybe on another version.
line = "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"  # Page line to break the text up a bit.
account = "Not Set"  # Account balance of coins
current_value = "not Set"  # For setting the value of each coin
interest_rate = "Not Set"  # For setting the intrest rate we will use.
display_interest_rate = "Not Set"  # For making it more readable
run_years = "Not Set"  # Amount of simulation years to run it for.
##


# Header- we call this a few times
time.sleep(1.5)
def header(coin, line, account,current_value, display_interest_rate, run_years): # Pass the data in to function
    
    print (f"{line}\n{coin} Compound Interest Staking Calculator\n{line}")
    print(f"Coin set to    : {coin}")
    print(f"coin balance   : {account}")
    print(f"Per coin value : £ {current_value}")
    print(f"Interest rate  : {display_interest_rate} %")
    print(f"Simulation yrs : {run_years}")
    print(f"{line}\n")
    return
##


# Get account balance from user.
while True: # Created a while loop to keep asking the question till a float is provided.
    clear_screen()
    header(coin, line, account, current_value, display_interest_rate, run_years)
    try:
        account = float(input(f"Please enter the amount of {coin} coins in account: "))
        clear_screen()
        header(coin, line, account, current_value, display_interest_rate, run_years)
        break

    except ValueError:
        print(f"Error: Please use a number.")
        time.sleep(1.5)
##   


# Get Interest rate from user.
while True: # Created a while loop to keep asking the question till a float is provided.
    clear_screen()
    header(coin, line, account, current_value, display_interest_rate, run_years)
    try:
        interest_rate = float(input(f"Please enter the amount of interest rate to apply: "))
        display_interest_rate = interest_rate *100
        clear_screen()
        header(coin, line, account, current_value, display_interest_rate, run_years)
        break

    except ValueError:
        print(f"Error: Please use a number.")
        time.sleep(1.5)
##


# Get current per coin value from user.
while True: # Created a while loop to keep asking the question till a float is provided.
    clear_screen()
    header(coin, line, account,current_value, display_interest_rate, run_years)
    try:
        current_value = float(input(f"Please enter the value of one coin: £"))
        
        clear_screen()
        header(coin, line, account,current_value, display_interest_rate, run_years )
        break

    except ValueError:
        print(f"Error: Please use a number.")
        time.sleep(1.5)
##


# Get amount of years to run the simulation for
while True: # Created a while loop to keep asking the question till a float is provided.
    clear_screen()
    header(coin, line, account, current_value, display_interest_rate, run_years)
    try:
        run_years = int(input(f"Please enter the amount of simulation years you want to run for: "))
        clear_screen()
        header(coin, line, account, current_value, display_interest_rate, run_years)
        break

    except ValueError:
        print(f"Error: Please use a number.")
        time.sleep(1.5)
##


# Information display section
time.sleep(0.3)
clear_screen()
print(line)
print("Please be aware this simulation does not take into\neffect that you may wish to add more coins over time\nor the interest rate might change.\n")
print("Simulation will show first year as weekly then\n following years as yearly.")
print(line)
time.sleep(2.5)
print (f"\nShowing Compound Interest For {run_years} yrs at {display_interest_rate} % rate")
print (f"Initial account balence: {account}\n")
start_account_bal = account # just so we can use this at the end
time.sleep(4)
print("Start of first year weekly simulation:\n")
time.sleep(2.5)
##


# Work out weekly and display
counter = 1
while counter <= 52:
    accured_interest = account * interest_rate
    weekly_bump = accured_interest / 52
    account += weekly_bump
    time.sleep(0.3)
    print (f"week {counter} Coins: {account}") 
    counter += 1 
##


# work out the yearly and display
print(f"\nNow simulating for rest of the {run_years-1} years.\n")
time.sleep(2.5)
# There is a slight diffrence as one weekly intrest and now we are working out a year.
counter = 2
while counter <= run_years:
    accured_interest = account * interest_rate
    account += accured_interest
    time.sleep(0.3)
    print (f"Year {counter} Coins: {account}")
    counter += 1
time.sleep(0.3)
##

# New variables required for final summary
difference = account - start_account_bal
total_weeks = run_years * 52
# final summary   
print(f"\n\n{line}")
print((f"Showing Compound intrest of {run_years} yrs at a rate of {display_interest_rate} %"))
print(f"\nInitial balance of {coin} was: {start_account_bal} coins.")
print(f"Final Balance of {coin} is:    {account} coins.\n")
print(f"This is a difference of:        {difference} coins.")
print(f"\nThe average amount of coins per week over {run_years} yrs")
print(f"would be {difference / total_weeks} coins per week.")

print(f"\n{line}")
print("CIC - created by User3xample\n\n")
