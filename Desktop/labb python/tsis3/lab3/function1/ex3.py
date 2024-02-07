def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        total_legs = 2 * num_chickens + 4 * num_rabbits
        if total_legs == numlegs:
            return num_chickens, num_rabbits
    return "No solution found"

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)

if isinstance(solution, tuple):
    num_chickens, num_rabbits = solution
    print("Number of chickens:", num_chickens)
    print("Number of rabbits:", num_rabbits)
else:
    print(solution)