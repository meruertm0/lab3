def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

input_numbers = input("Enter numbers separated by spaces: ")
nums = list(map(int, input_numbers.split()))
print(has_33(nums))
#print(has_33([1, 3, 3])) 
#print(has_33([1, 3, 1, 3])) 
#print(has_33([3, 1, 3]))
