def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return None, None

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(f"There are {chickens} chickens and {rabbits} rabbits.")
