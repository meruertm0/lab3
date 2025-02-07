from itertools import permutations

def print_permutations(s):
    perm_list = permutations(s)
    for perm in perm_list:
        print(''.join(perm))

s = input("Enter a string: ")
print("Permutations of the string are:")
print_permutations(s)
