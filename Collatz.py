# Collatz's Conjecture: 
# given any natural number n
# - if n is even, divide it by two
# - if n is odd, multiply it by 3 and then add one unit
# repeating it for an i amount of steps, the final result will always be one
# 
# although this conjecture doesn't have any proof to its support, nor any counterproof has been found,
# an empirical approach shows it to be consistent even up to n = 10^20

n = int(input("insert a positive number: "))
total = n
i = 0
while total != 1:
    if total % 2 == 0:
        total //= 2
    else:
        total = (total * 3) + 1
    i += 1
    print("iteration ", i)
    print(total)

# the time complexity of this algorithm only depends on the growt/shrink rate of the value of total, 
# since every operation inside the while loop takes a constant time complexity O(1).
# there actually is no way to determine how many times total is odd or even, but generally the time complexity
# is believed to be O(log n), as the growth of the number of iterations tends to grow logarithmically with the size of n.
#
# Although note that there is no definitive answer as to what the actual time complexity could be, that based on the fact that
# there is no proof that n always equals to 1. In fact, the algorithm may even run forever, given an unknown value of n 
# (I say unknown because such value would serve as a counterproof to Collatz's conjecture, invalidating it)