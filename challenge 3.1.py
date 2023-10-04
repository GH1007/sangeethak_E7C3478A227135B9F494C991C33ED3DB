def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
def search(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)
import re
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
arr_str = ','.join(str(i) for i in arr)
match = re.search(r'\b{}\b'.format(x), arr_str)
if match:
    result = arr_str[:match.start()].count(',')
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")