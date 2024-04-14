def linear(arr, target_num):
    for i in range(len(arr)):
        if arr[i] == target_num:
            return i
    return -1

arr = [10, 20, 3, 5]
target_num = 3

final_res = linear(arr, target_num)

if final_res == -1:
    print("Target not found")
else:
    print("Target found at index:", final_res)
