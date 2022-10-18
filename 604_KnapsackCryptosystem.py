SIK = input("Enter the Super-Increasing Knapsack: ").split(' ') 
# enter the space-separated list

# Creating the GK (General Knapsack)

## Choose a number n greater than sum(SIK)
sum_SIK = sum(SIK)
while True:
    n = int(input("Enter a number greater than ", sum_SIK, ": "))
    if n>sum_SIK:
        break

## Choose a number 