# Collatz's Conjecture: 
# Given any natural number n:
# - if n is even, divide it by two
# - if n is odd, multiply it by 3 and then add one
# Repeating this process for a number of steps, the final result should always be 1.
# 
# Although this conjecture has not been formally proven, nor has a counterexample been found,
# empirical evidence shows that it holds true for values up to n = 10^20.

n = int(input("Insert a positive number: "))
total = n
i = 0  # Iteration counter to track the number of steps
while total != 1:
    if total % 2 == 0:
        total //= 2
    else:
        total = (total * 3) + 1
    i += 1
    print("Iteration", i)
    print(total)

# The time complexity of this algorithm depends on how fast the value of 'total' grows or shrinks.
# Since every operation inside the while loop is constant time O(1), the overall time complexity
# is dominated by the number of iterations the loop runs. 
#
# Although the exact number of iterations is unpredictable (since we can't determine how often 
# 'total' will be odd or even), the growth of the sequence generally behaves logarithmically.
# Therefore, the time complexity is believed to be O(log n), where n is the starting value of 'total'.
#
# However, this is an empirical observation, not a proven result, because the conjecture itself remains unproven.
# If an unknown value of n exists that never reaches 1, this would disprove the conjecture and invalidate the algorithm.
