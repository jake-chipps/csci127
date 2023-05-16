# ------------------------------------
# Joy and Beauty of Data
# Author: Jake Chipps
# ------------------------------------
# Cash Register
# ------------------------------------

# Get user input for change

change = float(input("Enter some amount of money: $"))

# Break change into dollars and cents, using only ints
dollars = int(change)
cents = int(round(100 * (change - dollars))) # Note: the round() function returns a floating point number so we need to recast as int

# Break down dollars

# Get twenties
twenties = dollars // 20
# Get remainder
dollars = dollars % 20

# Get tens and find remainder
tens = dollars // 10
dollars = dollars % 10

# Get fives and find remainder
fives = dollars // 5
dollars = dollars % 5

# Get ones
ones = dollars

# Break down cents

# Get quarters and find remainder
quarters = cents // 25
cents = cents % 25

# Get dimes and find remainder
dimes = cents // 10
cents = cents % 10

# Get nickels and find remainder
nickels = cents // 5
cents = cents % 5

# Get pennies
pennies = cents

# Print it all out
print("$", change, "breaks down to: \n",
      twenties, "$20 bills\n",
      tens, "$10 bills\n",
      fives, "$5 bills\n",
      ones, "$1 bills\n",
      quarters, "quarters\n",
      dimes, "dimes\n",
      nickels, "nickels\n",
      pennies, "pennies")
