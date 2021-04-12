
# coding: utf-8

# In[1]:


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list

    items = reverse_mergesort(input_list)
    list1 = list()
    list2 = list()

    for item in items:
        if len(list1) > len(list2):
            list2.append(str(item))
        else:
            list1.append(str(item))

    return [int("".join(list1)), int("".join(list2))]


def reverse_mergesort(items):
    if len(items) <= 1:
        return items

    index = len(items) // 2
    left = items[:index]
    right = items[index:]

    left = reverse_mergesort(left)
    right = reverse_mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
print('Normal Cases:')
print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(list_num)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(list_num)
if result == [852, 964]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(list_num)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")

# Edge cases
print('Edge Cases:')
print('Test 4:')
list_num = [1, 1, 1]
result = rearrange_digits(list_num)
if result == [11, 1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 5:')
list_num = [1]
result = rearrange_digits(list_num)
if result == [1]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 6:')
list_num = []
result = rearrange_digits(list_num)
if result == []:
    print('Pass \n')
else:
    print("Fail \n")

