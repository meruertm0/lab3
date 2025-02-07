def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

original_list = [1, 2, 2, 3, 4, 4, 5]
print(f"Original list: {original_list}")
print(f"Unique elements: {unique_elements(original_list)}")
