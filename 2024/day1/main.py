with open("./day1.txt", "r") as file:
    # Split up the left and right side in to sep lists:
    left_list = []
    right_list = []
    for line in file:
        left_list.append(line.strip().split("   ")[0])
        right_list.append(line.strip().split("   ")[1])

# Sort them small to large
left_list.sort()
right_list.sort()

# Accumulator
total = 0

# Add to running total the absolute value of the difference
for index in range(len(left_list)):
    total += abs(int(left_list[index]) - int(right_list[index]))

print(total)
