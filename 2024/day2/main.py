# Ensure all are increasing or decreasing
# Ensure Each number next to each other must differ by 1 but no more than 3

input_data = []
input_data = open("./full_input.txt", "r").read()

list_to_check = []

# first split by new line, then split by spaces
for arr in input_data.split("\n"):
    temp = []
    for val in arr.split(" "):
        temp.append(int(val))
    list_to_check.append(temp)

safe_count = 0


def checkSafe(arr):
    ascending = True
    descending = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            ascending = False
        if arr[i] < arr[i + 1]:
            descending = False
        if abs(arr[i] - arr[i + 1]) > 3 or abs(arr[i] - arr[i + 1]) < 1:
            return False

    return ascending or descending


for arr in list_to_check:
    if checkSafe(arr):
        safe_count += 1


print(safe_count)
